"""

The MIT License (MIT)

Copyright (c) 2016, Mark Rogaski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from __future__ import unicode_literals

from django.conf import settings


# API service endpoints
BASE_URI = getattr(settings, 'DISCORD_BASE_URI',
                   'https://discordapp.com/api')
AUTHZ_URI = getattr(settings, 'DISCORD_AUTHZ_URI',
                    BASE_URI + '/oauth2/authorize')
TOKEN_URI = getattr(settings, 'DISCORD_TOKEN_URI',
                    BASE_URI + '/oauth2/token')

# OAuth2 application credentials
CLIENT_ID = getattr(settings, 'DISCORD_CLIENT_ID', '')
CLIENT_SECRET = getattr(settings, 'DISCORD_CLIENT_SECRET', '')

# OAuth2 scope
AUTHZ_SCOPE = (
    ['email', 'guilds.join'] if getattr(settings, 'DISCORD_EMAIL_SCOPE', True)
    else ['identity', 'guilds.join'])

# Return URI
INVITE_URI = getattr(settings, 'DISCORD_INVITE_URI',
                     'https://discordapp.com/channels/@me')
RETURN_URI = getattr(settings, 'DISCORD_RETURN_URI', '/')
