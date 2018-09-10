.. _installation:

Installation
------------

1.  Install with pip.

.. code-block:: console

    pip install django-discord-bind

2.  Add `discord_bind` to your `INSTALLED_APPS` setting:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'discord_bind',
    ]

3.  Include the URL configuration in your project **urls.py**:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^discord/', include('discord_bind.urls')),
    ]

4.  Run ``python manage.py migrate`` to create the discord_bind models.
