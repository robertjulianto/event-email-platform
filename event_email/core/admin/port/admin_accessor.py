from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class GetAdminAccessorSpec:
    email: str
    password: str


@dataclass
class GetAdminAccessorResult:
    id: Optional[int]


class IAdminAccessor(ABC):

    @abstractmethod
    def get_admin(self, accessor_spec: GetAdminAccessorSpec) -> GetAdminAccessorResult:
        raise NotImplementedError
