django-discord-bind
===================

*A Django app for securely associating a user with a Discord account.*

.. image:: https://badge.fury.io/py/django-discord-bind.svg
    :target: https://badge.fury.io/py/django-discord-bind
    :alt: Git Repository
.. image:: https://travis-ci.org/mrogaski/django-discord-bind.svg?branch=master
    :target: https://travis-ci.org/mrogaski/django-discord-bind
    :alt: Build Status
.. image:: https://readthedocs.org/projects/django-discord-bind/badge/?version=latest
    :target: http://django-discord-bind.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

This is a simple Django application that allows users to associate one or
more Discord accounts to their Django accounts and automatically join a
partner Discord server using the
`OAuth2 functionality of the Discord API <https://discordapp.com/developers/docs/topics/oauth2>`_.

This package does not provide any support for Discord as an identity provider, for that I
recommend `django-allauth <https://django-allauth.readthedocs.io/en/latest/>`_.

Requirements
------------

* Python 2.7, 3.5, 3.6, and 3.7
* Django 1.11, 2.0, and 2.1

License
-------

django-discord-bind is released under the terms of the MIT license.
Full details in LICENSE file.

