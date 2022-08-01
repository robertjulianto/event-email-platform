from flask import Blueprint
from flask_apispec import marshal_with, use_kwargs
from marshmallow import fields, post_load

from event_email.app.api.common.exceptions import FailResponse
from event_email.app.api.common.models import EventEmailSchema
from event_email.app.api.di import injector
from event_email.core.admin.port.admin_service import IAdminService, LoginSpec, LoginResult
from event_email.core.common.exceptions import LoginFailException

blp = Blueprint('admin', __name__)

admin_service = injector.get(IAdminService)  # type: ignore


class LoginRequest(EventEmailSchema):
    username = fields.Str()
    password = fields.Str()

    @post_load
    def __construct_spec(self, data, **kwargs) -> LoginSpec:
        return LoginSpec(**data)


class LoginResponse(EventEmailSchema):
    token = fields.Str()


@blp.post('/login')
@use_kwargs(LoginRequest)
@marshal_with(LoginResponse)
def login(spec: LoginSpec) -> LoginResult:
    try:
        return admin_service.login(spec=spec)
    except LoginFailException as e:
        raise FailResponse(str(e), error_code=e.error_code, status_code=401)

