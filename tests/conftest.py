from __future__ import absolute_import, unicode_literals

import pytest


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass
