from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.core.event.port.event_accessor import IEventAccessor
from event_email.infrastructure.event.adapter.event_accessor import EventAccessor


class EventInfrastructureModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(IEventAccessor, to=EventAccessor, scope=singleton)
