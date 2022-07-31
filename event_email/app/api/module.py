from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.app.api.common.adapter import SessionManager
from event_email.core.common.port.logger import ILogger
from event_email.core.email.adapter.email_service import EmailService
from event_email.core.email.port.email_service import IEmailService
from event_email.core.event.adapter.event_service import EventService
from event_email.core.event.port.event_service import IEventService
from event_email.infrastructure.common.adapter.logger import Logger
from event_email.infrastructure.sqlalchemy.port import ISessionManager


class EventEmailModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(ISessionManager, to=SessionManager, scope=singleton)
        binder.bind(ILogger, to=Logger, scope=singleton)
        binder.bind(IEmailService, to=EmailService, scope=singleton)
        binder.bind(IEventService, to=EventService, scope=singleton)
