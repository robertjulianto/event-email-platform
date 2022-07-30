import os

import pytest
from injector import Injector

from event_email.infrastructure.sqlalchemy.port import ISessionManager
from tests.adapter.session_manager import FakeSessionManager
from tests.module import TestEventEmailModule


@pytest.fixture
def injector():
    os.environ['APP_ENV'] = 'unittest'
    injector = Injector([
        TestEventEmailModule,
    ])
    yield injector
    session_manager: FakeSessionManager = injector.get(ISessionManager)  # noqa
    session_manager.tear_down()


@pytest.fixture
def session_manager(injector: Injector):
    return injector.get(ISessionManager)  # type: ignore
