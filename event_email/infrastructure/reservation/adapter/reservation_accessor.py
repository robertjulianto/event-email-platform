from injector import inject
from sqlalchemy import select

from event_email.core.common.models import Reservation, User
from event_email.infrastructure.reservation.port.reservation_accessor import IReservationAccessor, \
    GetReservationEmailsByEventIdAccessorSpec, GetReservationEmailsByEventIdAccessorResult
from event_email.infrastructure.sqlalchemy.port import ISessionManager


class ReservationAccessor(IReservationAccessor):

    @inject
    def __init__(
            self,
            session_manager: ISessionManager
    ):
        self.session_manager = session_manager

    def get_reservation_emails_by_event_id(
            self,
            accessor_spec: GetReservationEmailsByEventIdAccessorSpec
    ) -> GetReservationEmailsByEventIdAccessorResult:
        get_reserved_users = select(User) \
            .join_from(User, Reservation) \
            .where(Reservation.event_id == accessor_spec.event_id)
        with self.session_manager.get_session_scope() as sess:
            reserved_users = sess.execute(get_reserved_users).scalars().all()
        return GetReservationEmailsByEventIdAccessorResult(
            user_email_addresses=[user.email for user in reserved_users]
        )
