from datetime import datetime

from pytest_bdd import scenario, given, parsers, when, then
from sqlalchemy import select

from event_email.core.common.models import Admin, Event, Email
from event_email.core.email.port.email_service import IEmailService, SaveEmailSpec
from tests.utils import convert_str_to_datetime


@scenario("email.feature", "Create Scheduled Email")
def test_create_scheduled_email():
    pass


@given(
    parsers.parse("I am {admin_name}"),
    converters={"admin_name": str},
    target_fixture="admin_spec"
)
def load_admin_spec(session_manager, admin_name):
    split_name = admin_name.split(' ')
    first_name, last_name = ' '.join(split_name[:-1]), split_name[-1]
    get_admin_query = select(Admin).where(Admin.first_name == first_name, Admin.last_name == last_name)
    with session_manager.get_session_scope() as sess:
        admin = sess.execute(get_admin_query).scalar()
    return admin


@given(
    parsers.parse("I have event named {event_name}"),
    converters={"event_name": str},
    target_fixture="event_spec"
)
def load_event_spec(session_manager, event_name):
    get_event_query = select(Event).where(Event.name == event_name)
    with session_manager.get_session_scope() as sess:
        event = sess.execute(get_event_query).scalar()
    return event


@given(
    parsers.parse("I want to send email on {date_time}"),
    converters={"date_time": str},
    target_fixture="date_time_spec"
)
def load_date_time_spec(date_time):
    return convert_str_to_datetime(dt_string=date_time)


@given(
    parsers.parse("Email subject is {email_subject}"),
    converters={"email_subject": str},
    target_fixture="email_subject_spec"
)
def load_email_subject_spec(email_subject):
    return email_subject


@given(
    parsers.parse("Email content is {email_content}"),
    converters={"email_content": str},
    target_fixture="email_content_spec"
)
def load_email_content_spec(email_content):
    return email_content


@when(
    "I create scheduled email",
    target_fixture="create_scheduled_email_result"
)
def i_create_scheduled_email(injector, admin_spec, event_spec, date_time_spec, email_subject_spec, email_content_spec):
    email_service = injector.get(IEmailService)
    return email_service.create_email(
        spec=SaveEmailSpec(
            event_id=event_spec.id,
            email_subject=email_subject_spec,
            email_content=email_content_spec,
            timestamp=date_time_spec,
            created_by=admin_spec.email
        )
    )


@then(
    "Scheduled email is created",
    target_fixture="email_data"
)
def scheduled_email_is_created(session_manager, create_scheduled_email_result):
    get_email_query = select(Email).where(Email.id == create_scheduled_email_result.email_id)
    with session_manager.get_session_scope() as sess:
        email = sess.execute(get_email_query).scalar()
    assert email
    assert email.created_at
    return email


@then(
    parsers.parse("The event name is {event_name}"),
    converters={"event_name": str}
)
def assert_event_id(session_manager, email_data, event_name):
    get_event_query = select(Event).where(Event.id == email_data.event_id)
    with session_manager.get_session_scope() as sess:
        event = sess.execute(get_event_query).scalar()
    assert event.name == event_name


@then(
    parsers.parse("The email subject is {email_subject}"),
    converters={"email_subject": str}
)
def assert_email_subject(email_data, email_subject):
    assert email_data.subject == email_subject


@then(
    parsers.parse("The email content is {email_content}"),
    converters={"email_content": str}
)
def assert_email_content(email_data, email_content):
    assert email_data.content == email_content


@then(
    parsers.parse("The timestamp is {timestamp}"),
    converters={"timestamp": str}
)
def assert_date_time(email_data, timestamp):
    assert email_data.timestamp == convert_str_to_datetime(dt_string=timestamp)


@then(
    parsers.parse("Created by {creator_email}"),
    converters={"creator_email": str}
)
def assert_created_by(email_data, creator_email):
    assert email_data.created_by == creator_email
