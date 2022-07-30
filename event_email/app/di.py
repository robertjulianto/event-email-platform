from injector import Injector

from event_email.app.module import EventEmailModule

injector = Injector([
    EventEmailModule,
])
