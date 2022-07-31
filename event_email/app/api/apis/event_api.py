from flask import Blueprint
from flask_apispec import marshal_with
from marshmallow import fields

from event_email.app.api.common.models import EventEmailSchema
from event_email.app.api.di import injector
from event_email.core.event.port.event_service import GetUpcomingEventsResult, IEventService

blp = Blueprint('event', __name__)

event_service = injector.get(IEventService)  # type: ignore


class GetUpcomingEventsResponseItem(EventEmailSchema):
    event_id = fields.Int()
    event_name = fields.Str()
    event_date_time = fields.DateTime()


class GetUpcomingEventsResponse(EventEmailSchema):
    events = fields.List(fields.Nested(GetUpcomingEventsResponseItem()))


@blp.post('/get_upcoming')
@marshal_with(GetUpcomingEventsResponse)
def create_scheduled_email() -> GetUpcomingEventsResult:
    return event_service.get_upcoming_events()
