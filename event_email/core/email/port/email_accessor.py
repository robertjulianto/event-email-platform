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


class IEmailAccessor(ABC):

    @abstractmethod
    def create_email(self, accessor_spec: CreateEmailAccessorSpec) -> CreateEmailAccessorResult:
        raise NotImplementedError
