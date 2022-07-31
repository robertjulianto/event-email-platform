from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class GetUpcomingEventsResultItem:
    event_id: int
    event_name: str
    event_date_time: datetime


@dataclass
class GetUpcomingEventsResult:
    events: List[GetUpcomingEventsResultItem]


class IEventService(ABC):

    @abstractmethod
    def get_upcoming_events(self) -> GetUpcomingEventsResult:
        raise NotImplementedError
