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


License
-------

django-discord-bind is released under the terms of the MIT license.
Full details in LICENSE file.

