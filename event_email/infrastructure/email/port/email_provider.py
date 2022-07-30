from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SendEmailProviderSpec:
    email_id: int


class IEmailProvider(ABC):

    @abstractmethod
    def send_email(self, provider_spec: SendEmailProviderSpec) -> None:
        raise NotImplementedError
