from injector import inject
from sqlalchemy import insert

from event_email.core.common.models import Email
from event_email.core.email.port.email_accessor import IEmailAccessor, CreateEmailAccessorSpec, \
    CreateEmailAccessorResult
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
