from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class GetReservationEmailsByEventIdAccessorSpec:
    event_id: int


@dataclass
class GetReservationEmailsByEventIdAccessorResult:
    user_email_addresses: List[str]


class IReservationAccessor(ABC):

    @abstractmethod
    def get_reservation_emails_by_event_id(
            self,
            accessor_spec: GetReservationEmailsByEventIdAccessorSpec
    ) -> GetReservationEmailsByEventIdAccessorResult:
        raise NotImplementedError
