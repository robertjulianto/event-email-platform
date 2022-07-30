from sqlalchemy import MetaData, Table, Column, String, DateTime, FetchedValue, Numeric, ForeignKey, BigInteger
from sqlalchemy.orm import mapper

from event_email.core.common.models import User, Admin, Event, Reservation, Email

metadata = MetaData(schema='event_email')

mapper(
    User,
    Table(
        'user', metadata,
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('email', String),
        Column('city', String),
        Column('country', String),
        Column('created_at', DateTime, FetchedValue()),
        Column('created_by', String, FetchedValue()),
        Column('updated_at', DateTime, FetchedValue()),
        Column('updated_by', String, FetchedValue())
    )
)

mapper(
    Admin,
    Table(
        'admin', metadata,
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('email', String),
        Column('city', String),
        Column('country', String),
        Column('created_at', DateTime, FetchedValue()),
        Column('created_by', String, FetchedValue()),
        Column('updated_at', DateTime, FetchedValue()),
        Column('updated_by', String, FetchedValue())
    )
)

mapper(
    Event,
    Table(
        'event', metadata,
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('name', String),
        Column('description', String),
        Column('date_time', DateTime),
        Column('venue', String),
        Column('venue_address', String),
        Column('venue_latitude', Numeric),
        Column('venue_longitude', Numeric),
        Column('city', String),
        Column('country', String),
        Column('pic', String),
        Column('pic_contact', String),
        Column('created_at', DateTime, FetchedValue()),
        Column('created_by', String, FetchedValue()),
        Column('updated_at', DateTime, FetchedValue()),
        Column('updated_by', String, FetchedValue())
    )
)

mapper(
    Reservation,
    Table(
        'reservation', metadata,
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('event_id', BigInteger, ForeignKey('event.id')),
        Column('user_id', BigInteger, ForeignKey('user.id')),
        Column('created_at', DateTime, FetchedValue()),
        Column('created_by', String, FetchedValue()),
        Column('updated_at', DateTime, FetchedValue()),
        Column('updated_by', String, FetchedValue())
    )
)

mapper(
    Email,
    Table(
        'email', metadata,
        Column('id', BigInteger, primary_key=True, autoincrement=True),
        Column('event_id', BigInteger, ForeignKey('event.id')),
        Column('subject', String),
        Column('content', String),
        Column('timestamp', DateTime),
        Column('created_at', DateTime, FetchedValue()),
        Column('created_by', String, FetchedValue()),
        Column('updated_at', DateTime, FetchedValue()),
        Column('updated_by', String, FetchedValue())
    )
)
