from injector import inject

from event_email.core.auth.port.authentication_service import IAuthenticationService, GenerateTokenResult, AdminContext, \
    GenerateTokenSpec
from event_email.core.auth.port.token_provider import ITokenProvider


class AuthenticationService(IAuthenticationService):

    @inject
    def __init__(
            self,
            token_provider: ITokenProvider
    ):
        self.token_provider = token_provider

    def generate_token(self, spec: GenerateTokenSpec) -> GenerateTokenResult:
        return GenerateTokenResult(
            token=self.token_provider.generate_token(
                payload=spec.__dict__
            )
        )

    def verify_token(self, token: str) -> AdminContext:
        payload_dict = self.token_provider.verify_token(token)
        return AdminContext(**payload_dict)
