from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.infrastructure.reservation.adapter.reservation_accessor import ReservationAccessor
from event_email.infrastructure.reservation.port.reservation_accessor import IReservationAccessor


class ReservationInfrastructureModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(IReservationAccessor, to=ReservationAccessor, scope=singleton)
