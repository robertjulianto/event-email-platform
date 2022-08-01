from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.core.auth.port.token_provider import ITokenProvider
from event_email.infrastructure.auth.adapter.token_provider import JWTProvider


class TokenInfrastructureModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(ITokenProvider, to=JWTProvider, scope=singleton)
