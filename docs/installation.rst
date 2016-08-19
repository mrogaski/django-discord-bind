.. _installation:

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
