from injector import inject

from event_email.core.admin.port.admin_accessor import IAdminAccessor, GetAdminAccessorSpec
from event_email.core.admin.port.admin_service import IAdminService, LoginSpec, LoginResult
from event_email.core.auth.port.authentication_service import IAuthenticationService, GenerateTokenSpec
from event_email.core.common.exceptions import LoginFailException


class AdminService(IAdminService):

    @inject
    def __init__(
            self,
            admin_accessor: IAdminAccessor,
            authentication_service: IAuthenticationService
    ):
        self.admin_accessor = admin_accessor
        self.authentication_service = authentication_service

    def login(self, spec: LoginSpec) -> LoginResult:
        admin = self.admin_accessor.get_admin(
            accessor_spec=GetAdminAccessorSpec(
                email=spec.username,
                password=spec.password
            )
        )
        if admin.id:
            generate_token_result = self.authentication_service.generate_token(
                spec=GenerateTokenSpec(
                    username=spec.username
                )
            )
            return LoginResult(token=generate_token_result.token)
        else:
            raise LoginFailException
