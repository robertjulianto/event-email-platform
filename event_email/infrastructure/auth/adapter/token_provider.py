import jwt
from injector import inject

from event_email.core.admin.port.admin_accessor import IAdminAccessor
from event_email.core.auth.port.token_provider import ITokenProvider
from event_email.core.common.exceptions import ExpiredTokenError, InvalidTokenError
from event_email.core.common.port.logger import ILogger


class JWTProvider(ITokenProvider):
    SECRET_KEY = "MY_SECRET_KEY"

    @inject
    def __init__(
            self,
            logger: ILogger,
            admin_accessor: IAdminAccessor
    ) -> None:
        self.logger = logger
        self.admin_accessor = admin_accessor

    def generate_token(self, payload: dict) -> str:
        token = jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm='HS256'
        )
        return token

    def verify_token(self, token: str) -> dict:
        try:
            return jwt.decode(
                jwt=token,
                key=self.SECRET_KEY,
                algorithms=['HS256'],
                verify=True
            )
        except jwt.ExpiredSignatureError:
            raise ExpiredTokenError
        except Exception as e:
            self.logger.error(f'Verify token with spec: token = {token} failed because:', e)
            raise InvalidTokenError
