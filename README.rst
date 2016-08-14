===================
django-discord-bind
===================

*A Django app for securely associating a user with a Discord account.*

.. image:: https://badge.fury.io/py/django-discord-bind.svg
    :target: https://badge.fury.io/py/django-discord-bind
.. image:: https://travis-ci.org/mrogaski/django-discord-bind.svg?branch=master
    :target: https://travis-ci.org/mrogaski/django-discord-bind


This is a simple Django application that allows users to associate one or
more Discord accounts to their Django accounts and automatically join a
partner Discord server using the
`OAuth2 functionality of the Discord API <https://discordapp.com/developers/docs/topics/oauth2>`_.

Requirements
------------

* Python 2.7, 3.4, 3.5
* Django 1.9, 1.10


Installation
------------

Install with pip::

    pip install django-discord-bind

Add `discord_bind` to your `INSTALLED_APPS` setting:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'discord_bind',
    ]

Include the URL configuration in your project **urls.py**:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^discord/', include('discord_bind.urls')),
    ]

Run ``python manage.py migrate`` to create the discord_bind models.


Configuration
-------------

Required Settings
^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^

DISCORD_AUTHZ_PATH
~~~~~~~~~~~~~~~~~~
The path of the authorization request service endpoint, which will be
appended to the DISCORD_BASE_URI setting.

Default: /oauth2/authorize

DISCORD_BASE_URI
~~~~~~~~~~~~~~~~
The base URI for the Discord API.

Default: https://discordapp.com/api

DISCORD_INVITE_URI
~~~~~~~~~~~~~~~~~~
The URI that the user will be redirected to after one or more successful
auto-invites.

Default: https://discordapp.com/channels/@me

DISCORD_RETURN_URI
~~~~~~~~~~~~~~~~~~
The URI that the user will be redirected to if no auto-invites are
attempted or successful.

Default: /

DISCORD_TOKEN_PATH
~~~~~~~~~~~~~~~~~~
The path of the access token request service endpoint, which will be
appended to the DISCORD_BASE_URI setting.

Default: /oauth2/token


License
-------

django-discord-bind is released under the terms of the MIT license.
Full details in LICENSE file.

