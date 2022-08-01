from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class SaveEmailSpec:
    event_id: int
    email_subject: str
    email_content: str
    timestamp: datetime


@dataclass
class SaveEmailResult:
    email_id: int


class IEmailService(ABC):

    @abstractmethod
    def create_email(self, spec: SaveEmailSpec, user_name: str) -> SaveEmailResult:
        raise NotImplementedError
