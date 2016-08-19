.. _settings:

Settings
========

.. currentmodule:: django.conf.settings

Django Discord Bind has a number of settings that control its behavior.


Required settings
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
    
DISCORD_AUTHZ_PATH
~~~~~~~~~~~~~~~~~~

    Default: ``/oauth2/authorize``

The path of the authorization request service endpoint, which will be
appended to the DISCORD_BASE_URI setting.

