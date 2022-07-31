from datetime import timezone, datetime

from injector import inject
from sqlalchemy import select

from event_email.core.common.models import Event
from event_email.core.event.port.event_accessor import IEventAccessor, GetUpcomingEventsAccessorResult, \
    GetUpcomingEventsAccessorResultItem
from event_email.infrastructure.sqlalchemy.port import ISessionManager


class EventAccessor(IEventAccessor):

    @inject
    def __init__(
            self,
            session_manager: ISessionManager
    ):
        self.session_manager = session_manager

    def get_upcoming_events(self) -> GetUpcomingEventsAccessorResult:
        get_upcoming_event_query = select(
            Event.id,
            Event.name,
            Event.date_time,
        ).where(
            Event.date_time > datetime.now(tz=timezone.utc)
        )
        with self.session_manager.get_session_scope() as sess:
            events = sess.execute(get_upcoming_event_query).all()
        return GetUpcomingEventsAccessorResult(
            events=[GetUpcomingEventsAccessorResultItem(**e) for e in events]
        )
