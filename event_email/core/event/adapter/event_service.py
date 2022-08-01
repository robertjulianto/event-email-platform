from injector import inject

from event_email.core.event.port.event_accessor import IEventAccessor
from event_email.core.event.port.event_service import IEventService, GetUpcomingEventsResult, \
    GetUpcomingEventsResultItem


class EventService(IEventService):

    @inject
    def __init__(
            self,
            event_accessor: IEventAccessor
    ):
        self.event_accessor = event_accessor

    def get_upcoming_events(self) -> GetUpcomingEventsResult:
        result = self.event_accessor.get_upcoming_events()
        return GetUpcomingEventsResult(
            events=[
                GetUpcomingEventsResultItem(
                    event_id=e.id,
                    event_name=e.name,
                    event_date_time=e.date_time
                )
                for e in result.events
            ]
        )
