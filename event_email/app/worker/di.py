from injector import Injector

from event_email.app.worker.module import EventEmailWorkerModule
from event_email.infrastructure.email.module import EmailInfrastructureModule
from event_email.infrastructure.reservation.module import ReservationInfrastructureModule

injector = Injector([
    EventEmailWorkerModule,
    EmailInfrastructureModule,
    ReservationInfrastructureModule
])
