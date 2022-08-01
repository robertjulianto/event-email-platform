from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    email: str
    city: str
    country: str
    created_by: str
    created_at: datetime
    updated_by: str
    updated_at: datetime


@dataclass
class Admin(User):
    password: str


@dataclass
class Event:
    id: int
    name: str
    description: str
    date_time: datetime
    venue: str
    venue_address: str
    venue_latitude: Decimal
    venue_longitude: Decimal
    city: str
    country: str
    pic: str
    pic_contact: str
    created_by: str
    created_at: datetime
    updated_by: str
    updated_at: datetime


@dataclass
class Reservation:
    id: int
    event_id: int
    user_id: str
    created_by: str
    created_at: datetime
    updated_by: str
    updated_at: datetime


@dataclass
class Email:
    id: int
    event_id: int
    subject: str
    content: str
    timestamp: datetime
    created_by: str
    created_at: datetime
    updated_by: str
    updated_at: datetime


@dataclass
class PaginatedSpec:
    page: int
    take: int


@dataclass
class PaginatedResult:
    page: int
    total: int
