from datetime import timezone

from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields, post_load

from event_email.app.api.common.models import EventEmailSchema
from event_email.app.api.di import injector
from event_email.app.worker.main_task import send_email

from event_email.core.email.port.email_service import IEmailService, SaveEmailSpec, SaveEmailResult

blp = Blueprint('email', __name__)

email_service = injector.get(IEmailService)  # type: ignore


class SaveEmailsRequest(EventEmailSchema):
    event_id = fields.Int(required=True)
    email_subject = fields.Str(required=True)
    email_content = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)

    @post_load
    def __construct_spec(self, data, **kwargs) -> SaveEmailSpec:
        data['created_by'] = 'ihumbles0@blogspot.com'
        return SaveEmailSpec(**data)


class SaveEmailsResponse(EventEmailSchema):
    email_id = fields.Int()


@blp.post('/save_emails')
@use_kwargs(SaveEmailsRequest)
@marshal_with(SaveEmailsResponse)
def create_scheduled_email(spec: SaveEmailSpec) -> SaveEmailResult:
    save_email_result = email_service.create_email(spec=spec)
    send_email.apply_async(
        kwargs={"email_id": save_email_result.email_id},
        eta=spec.timestamp.astimezone(tz=timezone.utc)
    )
    return save_email_result
