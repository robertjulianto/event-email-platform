from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.app.api.common.adapter import SessionManager
from event_email.core.common.port.logger import ILogger
from event_email.infrastructure.common.adapter.logger import Logger
from event_email.infrastructure.sqlalchemy.port import ISessionManager


class EventEmailWorkerModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(ISessionManager, to=SessionManager, scope=singleton)
        binder.bind(ILogger, to=Logger, scope=singleton)
