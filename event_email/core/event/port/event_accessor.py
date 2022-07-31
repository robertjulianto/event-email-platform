from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class GetUpcomingEventsAccessorResultItem:
    id: int
    name: str
    date_time: datetime


@dataclass
class GetUpcomingEventsAccessorResult:
    events: List[GetUpcomingEventsAccessorResultItem]


class IEventAccessor(ABC):

    @abstractmethod
    def get_upcoming_events(self) -> GetUpcomingEventsAccessorResult:
        raise NotImplementedError
