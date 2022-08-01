from datetime import datetime, timezone

from injector import inject
from sqlalchemy import insert, select, func, desc, update

from event_email.core.common.models import Email, Event
from event_email.core.email.port.email_accessor import IEmailAccessor, CreateEmailAccessorSpec, \
    CreateEmailAccessorResult, GetEmailByIdAccessorResult, GetEmailByIdAccessorSpec, GetPaginatedEmailsAccessorSpec, \
    GetPaginatedEmailsAccessorResult, GetPaginatedEmailsAccessorResultItem, UpdateSentAtEmailAccessorSpec
from event_email.infrastructure.sqlalchemy.port import ISessionManager


class EmailAccessor(IEmailAccessor):

    @inject
    def __init__(
            self,
            session_manager: ISessionManager
    ):
        self.session_manager = session_manager

    def create_email(self, accessor_spec: CreateEmailAccessorSpec) -> CreateEmailAccessorResult:
        insert_email_query = insert(Email).values(
            **accessor_spec.__dict__
        ).returning(Email.id)
        with self.session_manager.get_session_scope() as sess:
            email_id_result = sess.execute(insert_email_query).scalar()
            sess.commit()
        return CreateEmailAccessorResult(
            email_id=email_id_result
        )

    def get_email_by_id(self, accessor_spec: GetEmailByIdAccessorSpec) -> GetEmailByIdAccessorResult:
        get_email_query = select(
            Email.event_id,
            Email.subject,
            Email.content,
            Email.created_by
        ).where(Email.id == accessor_spec.email_id)
        with self.session_manager.get_session_scope() as sess:
            result = sess.execute(get_email_query).first()
        return GetEmailByIdAccessorResult(**result)

    def get_paginated_emails(self, accessor_spec: GetPaginatedEmailsAccessorSpec) -> GetPaginatedEmailsAccessorResult:
        offset_value = (accessor_spec.page - 1) * accessor_spec.take
        get_emails_query = select(
            Email.id.label('email_id'),  # type: ignore
            Event.name.label('event_name'),  # type: ignore
            Email.subject.label('email_subject'),  # type: ignore
            Email.content.label('email_content'),  # type: ignore
            Email.created_at,
            Email.created_by,
            Email.sent_at
        ).join_from(Email, Event).order_by(desc(Email.created_at)).limit(accessor_spec.take).offset(offset_value)
        with self.session_manager.get_session_scope() as sess:
            total = sess.execute(select(func.count(Email.id))).scalar()
            emails = sess.execute(get_emails_query).all()
        return GetPaginatedEmailsAccessorResult(
            page=accessor_spec.page,
            total=total,
            emails=[GetPaginatedEmailsAccessorResultItem(**e) for e in emails]
        )

    def update_sent_at_email(self, accessor_spec: UpdateSentAtEmailAccessorSpec) -> None:
        update_email_query = update(Email).values(
            updated_by="WORKER",
            sent_at=datetime.now(tz=timezone.utc)
        ).where(
            Email.id == accessor_spec.id
        )
        with self.session_manager.get_session_scope() as sess:
            sess.execute(update_email_query)
            sess.commit()

