from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.core.email.port.email_accessor import IEmailAccessor
from event_email.infrastructure.email.adapter.email_accessor import EmailAccessor
from event_email.infrastructure.email.adapter.email_provider import EmailProvider
from event_email.infrastructure.email.port.email_provider import IEmailProvider


class EmailInfrastructureModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(IEmailAccessor, to=EmailAccessor, scope=singleton)
        binder.bind(IEmailProvider, to=EmailProvider, scope=singleton)
