# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

DATABASES = {
    'default': {
        'NAME': 'test.db',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'discord_bind',
)

SECRET_KEY = 'vn5v8g+q3q*ll)a3kh10wlj#(tc=738cklg9(z3***kw%qhnv-'

ROOT_URLCONF = 'discord_bind.urls'

DISCORD_CLIENT_ID = '212763200357720576'
