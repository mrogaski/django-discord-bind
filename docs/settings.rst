.. _settings:

Settings
========

.. currentmodule:: django.conf.settings

Django Discord Bind has a number of settings that control its behavior.


Required Settings
-----------------

DISCORD_CLIENT_ID
~~~~~~~~~~~~~~~~~

The client identifier issued by the Discord authorization server.  This
identifier is used in the authorization request of the OAuth 2.0
Authorization Code Grant workflow.

DISCORD_CLIENT_SECRET
~~~~~~~~~~~~~~~~~~~~~

A shared secret issued by the Discord authorization server.  This
identifier is used in the access token request of the OAuth 2.0
Authorization Code Grant workflow.

Optional Settings
-----------------

DISCORD_AUTHZ_PATH
~~~~~~~~~~~~~~~~~~

    Default: ``/oauth2/authorize``

The path of the authorization request service endpoint, which will be
appended to the DISCORD_BASE_URI setting.

DISCORD_BASE_URI
~~~~~~~~~~~~~~~~

    Default: ``https://discordapp.com/api``

The base URI for the Discord API.

DISCORD_INVITE_URI
~~~~~~~~~~~~~~~~~~

    Default: ``https://discordapp.com/channels/@me``

The URI that the user will be redirected to after one or more successful
auto-invites.

DISCORD_REDIRECT_URI
~~~~~~~~~~~~~~~~~~

    Default: ``reverse('discord_bind_callback')``

The URI that will be passed to the Discord authorization endpoint as the 
URI for the callback route.  Normally this is determined by Django, but
it can be set manually if the application is behind a proxy.

DISCORD_RETURN_URI
~~~~~~~~~~~~~~~~~~

    Default: ``/``

The URI that the user will be redirected to if no auto-invites are
attempted or successful.

DISCORD_TOKEN_PATH
~~~~~~~~~~~~~~~~~~

    Default: ``/oauth2/token``

The path of the access token request service endpoint, which will be
appended to the DISCORD_BASE_URI setting.
