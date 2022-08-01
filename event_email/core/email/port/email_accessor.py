from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from event_email.core.common.models import PaginatedSpec, PaginatedResult


@dataclass
class CreateEmailAccessorSpec:
    event_id: int
    subject: str
    content: str
    timestamp: datetime
    created_by: str


@dataclass
class CreateEmailAccessorResult:
    email_id: int


@dataclass
class GetEmailByIdAccessorSpec:
    email_id: int


@dataclass
class GetEmailByIdAccessorResult:
    event_id: int
    subject: str
    content: str
    created_by: str


@dataclass
class GetPaginatedEmailsAccessorSpec(PaginatedSpec):
    pass


@dataclass
class GetPaginatedEmailsAccessorResultItem:
    email_id: str
    event_name: str
    email_subject: str
    email_content: str
    created_at: datetime
    created_by: str


@dataclass
class GetPaginatedEmailsAccessorResultItem:
    email_id: str
    event_name: str
    email_subject: str
    email_content: str
    created_at: datetime
    created_by: str


@dataclass
class GetPaginatedEmailsAccessorResult(PaginatedResult):
    emails: List[Optional[GetPaginatedEmailsAccessorResultItem]]


class IEmailAccessor(ABC):

    @abstractmethod
    def create_email(self, accessor_spec: CreateEmailAccessorSpec) -> CreateEmailAccessorResult:
        raise NotImplementedError

    @abstractmethod
    def get_email_by_id(self, accessor_spec: GetEmailByIdAccessorSpec) -> GetEmailByIdAccessorResult:
        raise NotImplementedError

    @abstractmethod
    def get_paginated_emails(self, accessor_spec: GetPaginatedEmailsAccessorSpec) -> GetPaginatedEmailsAccessorResult:
        raise NotImplementedError
