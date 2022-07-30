from injector import inject
from sqlalchemy import insert, select

from event_email.core.common.models import Email
from event_email.core.email.port.email_accessor import IEmailAccessor, CreateEmailAccessorSpec, \
    CreateEmailAccessorResult, GetEmailByIdAccessorResult, GetEmailByIdAccessorSpec
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
            result = sess.execute(get_email_query).scalar()
        return GetEmailByIdAccessorResult(**result)
