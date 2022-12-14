from injector import Injector

from event_email.app.api.module import EventEmailModule
from event_email.infrastructure.admin.module import AdminInfrastructureModule
from event_email.infrastructure.auth.module import TokenInfrastructureModule
from event_email.infrastructure.email.module import EmailInfrastructureModule
from event_email.infrastructure.event.module import EventInfrastructureModule

injector = Injector([
    EventEmailModule,
    EmailInfrastructureModule,
    EventInfrastructureModule,
    AdminInfrastructureModule,
    TokenInfrastructureModule,
])
