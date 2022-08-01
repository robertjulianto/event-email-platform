from datetime import timezone

from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields, post_load, validate

from event_email.app.api.common.decorators import authenticate
from event_email.app.api.common.models import EventEmailSchema
from event_email.app.api.di import injector
from event_email.app.worker.main_task import send_email
from event_email.core.auth.port.authentication_service import AdminContext
from event_email.core.email.port.email_service import IEmailService, SaveEmailSpec, SaveEmailResult, \
    GetPaginatedEmailSpec, GetPaginatedEmailResult

blp = Blueprint('email', __name__)

email_service = injector.get(IEmailService)


class SaveEmailsRequest(EventEmailSchema):
    event_id = fields.Int(required=True)
    email_subject = fields.Str(required=True)
    email_content = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)

    @post_load
    def __construct_spec(self, data, **kwargs) -> SaveEmailSpec:
        return SaveEmailSpec(**data)


class SaveEmailsResponse(EventEmailSchema):
    email_id = fields.Int()


@blp.post('/save_emails')
@authenticate()
@use_kwargs(SaveEmailsRequest)
@marshal_with(SaveEmailsResponse)
def create_scheduled_email(spec: SaveEmailSpec, admin_context: AdminContext) -> SaveEmailResult:
    save_email_result = email_service.create_email(spec=spec, username=admin_context.username)
    send_email.apply_async(
        kwargs={"email_id": save_email_result.email_id},
        eta=spec.timestamp.astimezone(tz=timezone.utc)
    )
    return save_email_result


class GetPaginatedEmailsRequestPaginatedSpec(EventEmailSchema):
    page = fields.Int(validate=validate.Range(min_inclusive=True, min=1))
    take = fields.Int(validate=validate.Range(min_inclusive=True, min=1))


class GetPaginatedEmailsRequest(EventEmailSchema):
    paginated_spec = fields.Nested(GetPaginatedEmailsRequestPaginatedSpec())

    @post_load
    def __construct_spec(self, data, **kwargs) -> GetPaginatedEmailSpec:
        return GetPaginatedEmailSpec(**data['paginated_spec'])


class GetPaginatedEmailsResponseEmailsItem(EventEmailSchema):
    email_id = fields.Int()
    event_name = fields.Str()
    email_subject = fields.Str()
    email_content = fields.Str()
    created_at = fields.DateTime()
    created_by = fields.Str()


class GetPaginatedEmailsResponse(EventEmailSchema):
    page = fields.Int()
    total = fields.Int()
    emails = fields.List(fields.Nested(GetPaginatedEmailsResponseEmailsItem()))


@blp.post('/get_paginated')
@use_kwargs(GetPaginatedEmailsRequest)
@marshal_with(GetPaginatedEmailsResponse)
def get_paginated_emails(spec: GetPaginatedEmailSpec) -> GetPaginatedEmailResult:
    return email_service.get_paginated_emails(spec=spec)
