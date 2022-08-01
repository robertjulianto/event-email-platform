from injector import inject
from sqlalchemy import select

from event_email.app.api.common.adapter import SessionManager
from event_email.core.admin.port.admin_accessor import IAdminAccessor, GetAdminAccessorSpec, GetAdminAccessorResult
from event_email.core.common.models import Admin


class AdminAccessor(IAdminAccessor):

    @inject
    def __init__(
            self,
            session_manager: SessionManager
    ):
        self.session_manager = session_manager

    def get_admin(self, accessor_spec: GetAdminAccessorSpec) -> GetAdminAccessorResult:
        get_admin_query = select(Admin.id).where(
            Admin.email == accessor_spec.email,
            Admin.password == accessor_spec.password
        )
        with self.session_manager.get_session_scope() as sess:
            admin_id = sess.execute(get_admin_query).scalar()
        return GetAdminAccessorResult(
            id=admin_id
        )

