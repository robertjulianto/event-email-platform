from typing import no_type_check

from injector import Module, Binder, singleton

from event_email.core.admin.port.admin_accessor import IAdminAccessor
from event_email.infrastructure.admin.adapter.admin_accessor import AdminAccessor


class AdminInfrastructureModule(Module):
    @no_type_check
    def configure(self, binder: Binder) -> None:
        binder.bind(IAdminAccessor, to=AdminAccessor, scope=singleton)
