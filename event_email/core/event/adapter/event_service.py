from dataclasses import dataclass
from datetime import datetime
from typing import List

from injector import inject

from event_email.core.event.port.event_accessor import IEventAccessor
from event_email.core.event.port.event_service import IEventService


@dataclass
class GetUpcomingEventResultItem:
    event_id: int
    event_name: str
    event_date_time: datetime


@dataclass
class GetUpcomingEventResult:
    events: List[GetUpcomingEventResultItem]


class EventService(IEventService):

    @inject
    def __init__(
            self,
            event_accessor: IEventAccessor
    ):
        self.event_accessor = event_accessor

    def get_upcoming_events(self) -> GetUpcomingEventResult:
        result = self.event_accessor.get_upcoming_events()
        return GetUpcomingEventResult(
            events=[
                GetUpcomingEventResultItem(
                    event_id=e.id,
                    event_name=e.name,
                    event_date_time=e.date_time
                )
                for e in result.events
            ]
        )
