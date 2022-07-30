from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


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


class IEmailAccessor(ABC):

    @abstractmethod
    def create_email(self, accessor_spec: CreateEmailAccessorSpec) -> CreateEmailAccessorResult:
        raise NotImplementedError

    @abstractmethod
    def get_email_by_id(self, accessor_spec: GetEmailByIdAccessorSpec) -> GetEmailByIdAccessorResult:
        raise NotImplementedError
