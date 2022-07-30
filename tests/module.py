from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.core.common.port.logger import ILogger
from event_email.core.email.adapter.email_service import EmailService
from event_email.core.email.port.email_service import IEmailService
from event_email.infrastructure.common.adapter.logger import Logger
from event_email.infrastructure.sqlalchemy.port import ISessionManager
from tests.adapter.session_manager import FakeSessionManager


class TestEventEmailModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(ISessionManager, to=FakeSessionManager, scope=singleton)
        binder.bind(ILogger, to=Logger, scope=singleton)
        binder.bind(IEmailService, to=EmailService, scope=singleton)
