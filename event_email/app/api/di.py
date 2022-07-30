from injector import Injector

from event_email.app.api.module import EventEmailModule
from event_email.infrastructure.email.module import EmailInfrastructureModule

injector = Injector([
    EventEmailModule,
    EmailInfrastructureModule
])
