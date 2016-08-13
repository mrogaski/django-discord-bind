===================
django-discord-bind
===================

This is a simple Django app that allows users to bind their Discord accounts
to their Django accounts and join a partner Discord server using the OAuth2
functionality of the Discord API.

Quick start
-----------

1. Add "discord_bind" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'discord_bind',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^discord/', include('discord_bind.urls')),

3. Run `python manage.py migrate` to create the discord_bind models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a Discord invite code (you'll need the Admin app enabled).

5. Visit https://discordapp.com/developers/applications/me to create
   an application.  Add http://127.0.0.1:8000/discord/cb as a redirect URI.

6. Add the Client ID and Secret values to the project settings.py file::

    DISCORD_CLIENT_ID = 212763200357720576
    DISCORD_CLIENT_SECRET = MfpBbcX2Ga3boNhoQoBTdHNUS2B1xX8f

5. Visit http://127.0.0.1:8000/discord/ to bind your Discord account and
   auto-accept the invite code.
