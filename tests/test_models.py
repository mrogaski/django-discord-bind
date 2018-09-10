# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from django.db import IntegrityError
import pytest

from discord_bind.models import DiscordUser, DiscordInvite


@pytest.fixture()
def user():
    return User.objects.create(username='henry')


@pytest.fixture()
def groups():
    return {
        'red': Group.objects.create(name='Red Team'),
        'blue': Group.objects.create(name='Blue Team')
    }


@pytest.fixture()
def invites(groups):
    DiscordInvite.objects.create(code='EzqS3tytSpUCa7Lr', active=True)

    inv = DiscordInvite.objects.create(code='8UQcx0Ychpq1Kmqs', active=True)
    inv.groups.add(groups['blue'])

    inv = DiscordInvite.objects.create(code='9dbFpT89bmXzejG9', active=False)
    inv.groups.add(groups['red'])

    inv = DiscordInvite.objects.create(code='pMqXoCQT41S7e4LK');
    inv.groups.add(groups['blue'])
    inv.groups.add(groups['red'])


def test_discord_user(user):
    u = DiscordUser.objects.create(user=user, uid='172150183260323840', username='Henry Tiger', discriminator='1738')
    assert str(u) == '%s.%s' % (u.username, u.discriminator)


def test_invite_status(invites):
    assert DiscordInvite.objects.filter(active=True).count() == 2
    assert DiscordInvite.objects.filter(active=False).count() == 2


def test_invite_groups(groups, invites):
    assert DiscordInvite.objects.filter(groups=groups['blue']).count() == 2
    assert DiscordInvite.objects.filter(groups=groups['red']).count() == 2
    assert DiscordInvite.objects.filter(groups__isnull=True).count() == 1


def test_duplicate_invite(invites):
    with pytest.raises(IntegrityError):
        DiscordInvite.objects.create(code='EzqS3tytSpUCa7Lr', active=True)


def test_invite_update(invites, requests_mock):
    data = {
        "code": "aY1XeQGDKL8iCRvJ",
        "guild": {
            "splash": None,
            "id": "132196927679889408",
            "icon": "b472e4221e5b24f4de1583be747ca1bd",
            "name": "Alea Iacta Est"
        },
        "channel": {
            "type": "text",
            "id": "132196927679889408",
            "name": "general"
        }
    }
    requests_mock.get('https://discordapp.com/api/invites/aY1XeQGDKL8iCRvJ', json=data)
    obj = DiscordInvite.objects.create(code='aY1XeQGDKL8iCRvJ')
    obj.update_context()

    assert obj.guild_id == '132196927679889408'
    assert obj.guild_name == 'Alea Iacta Est'
    assert obj.guild_icon == 'b472e4221e5b24f4de1583be747ca1bd'
    assert obj.channel_id == '132196927679889408'
    assert obj.channel_name == 'general'
    assert obj.channel_type == 'text'
