from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class GenerateTokenSpec:
    username: str


@dataclass
class GenerateTokenResult:
    token: str


@dataclass
class AdminContext:
    admin_email: str


class IAuthenticationService(ABC):

    @abstractmethod
    def generate_token(self, spec: GenerateTokenSpec) -> GenerateTokenResult:
        raise NotImplementedError

    @abstractmethod
    def verify_token(self, token: str) -> AdminContext:
        raise NotImplementedError
