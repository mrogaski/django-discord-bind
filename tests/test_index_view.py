# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import os

import pytest
from django.test import TestCase, RequestFactory, override_settings
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse

from discord_bind.views import index


@pytest.fixture()
def user():
    return User.objects.create_user(username="Hoots", email="hoots@example.com", password="test")


@pytest.fixture()
def factory(rf):
    def f(user=None, query=None):
        url = reverse('discord_bind_index')
        if user is None:
            user = AnonymousUser()
        if query is not None:
            url = url + '?' + query
        request = rf.get(url)
        request.user = user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        return request

    return f


def test_unauthenticated_user(factory):
    request = factory()
    response = index(request)
    assert response.status_code == 302
    assert 'login' in response['location']


def test_authenticated_user(factory, user):
    request = factory(user=user)
    response = index(request)
    assert response.status_code == 302
    assert response['location'].startswith('https://discordapp.com/api/oauth2/authorize')
    assert 'response_type=code' in response['location']
    assert 'client_id=212763200357720576' in response['location']
    assert 'redirect_uri=http%3A%2F%2Ftestserver%2Fcb' in response['location']
    assert 'scope=email+guilds.join' in response['location']
    assert 'state={}'.format(request.session['discord_bind_oauth_state']) in response['location']


def test_limited_scope(settings, factory, user):
    settings.DISCORD_EMAIL_SCOPE = False
    request = factory(user)
    response = index(request)
    assert 'scope=identity+guilds.join' in response['location']


def test_base_uri(settings, factory, user):
    settings.DISCORD_BASE_URI = 'https://www.example.com/api'
    request = factory(user)
    response = index(request)
    assert response['location'].startswith('https://www.example.com/api/oauth2/authorize')


def test_authz_path(settings, factory, user):
    settings.DISCORD_AUTHZ_PATH = '/foo/bar'
    request = factory(user)
    response = index(request)
    assert response['location'].startswith('https://discordapp.com/api/foo/bar')


def test_valid_redirect(settings, factory, user):
    settings.DISCORD_REDIRECT_URI = 'https://foo.bar/cb'
    request = factory(user)
    response = index(request)
    assert 'redirect_uri=https%3A%2F%2Ffoo.bar%2Fcb' in response['location']


def test_invalid_redirect(factory, user):
    request = factory(user, query='redirect_uri=https://foo.bar/cb')
    response = index(request)
    assert 'redirect_uri=https%3A%2F%2Ffoo.bar%2Fcb' not in response['location']


def test_invite_uri(factory, user):
    request = factory(user)
    response = index(request)
    assert request.session['discord_bind_invite_uri'] == 'https://discordapp.com/channels/@me'


def test_invite_uri_configuration(settings, factory, user):
    settings.DISCORD_INVITE_URI = 'https://www.example.com/'
    request = factory(user)
    response = index(request)
    assert request.session['discord_bind_invite_uri'] == 'https://www.example.com/'


def test_invite_uri_parameter(factory, user):
    request = factory(user, query='invite_uri=/foo')
    response = index(request)
    assert request.session['discord_bind_invite_uri'] == '/foo'


def test_return_uri(factory, user):
    request = factory(user)
    response = index(request)
    assert request.session['discord_bind_return_uri'] == '/'


def test_return_uri_configuration(settings, factory, user):
    settings.DISCORD_RETURN_URI = 'https://www.example.com/'
    request = factory(user)
    response = index(request)
    assert request.session['discord_bind_return_uri'] == 'https://www.example.com/'


def test_return_uri_parameter(factory, user):
    request = factory(user, query='return_uri=/foo')
    response = index(request)
    assert request.session['discord_bind_return_uri'] == '/foo'
