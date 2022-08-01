from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from event_email.core.common.models import PaginatedSpec, PaginatedResult


@dataclass
class SaveEmailSpec:
    event_id: int
    email_subject: str
    email_content: str
    timestamp: datetime


@dataclass
class SaveEmailResult:
    email_id: int


@dataclass
class GetPaginatedEmailSpec(PaginatedSpec):
    pass


@dataclass
class GetPaginatedEmailResultItem:
    email_id: str
    event_name: str
    email_subject: str
    email_content: str
    created_at: datetime
    created_by: str
    sent_at: Optional[datetime]


@dataclass
class GetPaginatedEmailResult(PaginatedResult):
    emails: List[Optional[GetPaginatedEmailResultItem]]


class IEmailService(ABC):

    @abstractmethod
    def create_email(self, spec: SaveEmailSpec, username: str) -> SaveEmailResult:
        raise NotImplementedError

    @abstractmethod
    def get_paginated_emails(self, spec: GetPaginatedEmailSpec) -> GetPaginatedEmailResult:
        raise NotImplementedError
