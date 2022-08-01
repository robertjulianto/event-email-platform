import inspect
from functools import wraps

from flask import request

from event_email.app.api.common.exceptions import FailResponse, ExpiredTokenException
from event_email.app.api.di import injector
from event_email.core.auth.port.authentication_service import IAuthenticationService
from event_email.core.common.exceptions import InvalidTokenError, ExpiredTokenError


def authenticate():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            authentication_service: IAuthenticationService = injector.get(IAuthenticationService)
            try:
                auth: str = request.headers.get('Authorization')
                if auth and auth.startswith('Bearer '):
                    token = auth.split(' ', maxsplit=1)[1]
                    admin_context = authentication_service.verify_token(token)
                else:
                    raise FailResponse('Invalid token.', 401, error_code='INVALID_TOKEN')
                if inspect.signature(f).parameters.get('admin_context'):
                    return f(*args, **kwargs, admin_context=admin_context)
                return f(*args, **kwargs)
            except InvalidTokenError:
                raise FailResponse('Invalid token.', 401, error_code='INVALID_TOKEN')
            except ExpiredTokenError:
                raise ExpiredTokenException

        return decorated_function

    return decorator
