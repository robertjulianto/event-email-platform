from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass
class LoginSpec:
    username: str
    password: str


@dataclass
class LoginResult:
    token: str


class IAdminService(ABC):

    @abstractmethod
    def login(self, spec: LoginSpec) -> LoginResult:
        raise NotImplementedError
