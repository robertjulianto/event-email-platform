from injector import inject

from event_email.core.common.exceptions import EventEmailGeneralException
from event_email.core.common.port.logger import ILogger
from event_email.core.email.port.email_accessor import IEmailAccessor, CreateEmailAccessorSpec, \
    GetPaginatedEmailsAccessorSpec
from event_email.core.email.port.email_service import IEmailService, SaveEmailSpec, SaveEmailResult, \
    GetPaginatedEmailResult, GetPaginatedEmailSpec, GetPaginatedEmailResultItem


class EmailService(IEmailService):

    @inject
    def __init__(
            self,
            logger: ILogger,
            email_accessor: IEmailAccessor
    ):
        self.logger = logger
        self.email_accessor = email_accessor

    def create_email(self, spec: SaveEmailSpec, username: str) -> SaveEmailResult:
        try:
            return SaveEmailResult(
                email_id=self.email_accessor.create_email(
                    accessor_spec=CreateEmailAccessorSpec(
                        event_id=spec.event_id,
                        subject=spec.email_subject,
                        content=spec.email_content,
                        timestamp=spec.timestamp,
                        created_by=username
                    )
                ).email_id
            )
        except EventEmailGeneralException as e:
            self.logger.error(msg=str(e), exception=e)
            raise e

    def get_paginated_emails(self, spec: GetPaginatedEmailSpec) -> GetPaginatedEmailResult:
        result = self.email_accessor.get_paginated_emails(
            accessor_spec=GetPaginatedEmailsAccessorSpec(**spec.__dict__))
        return GetPaginatedEmailResult(
            page=result.page,
            total=result.total,
            emails=[GetPaginatedEmailResultItem(**e.__dict__) for e in result.emails]
        )
