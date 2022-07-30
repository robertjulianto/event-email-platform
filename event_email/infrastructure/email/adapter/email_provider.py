import os
import smtplib
from email.message import EmailMessage

from injector import inject

from event_email.core.email.port.email_accessor import IEmailAccessor, GetEmailByIdAccessorSpec
from event_email.infrastructure.email.port.email_provider import IEmailProvider, SendEmailProviderSpec
from event_email.infrastructure.reservation.port.reservation_accessor import IReservationAccessor, \
    GetReservationEmailsByEventIdAccessorSpec


class EmailProvider(IEmailProvider):

    @inject
    def __init__(
            self,
            email_accessor: IEmailAccessor,
            reservation_accessor: IReservationAccessor
    ):
        self.email_accessor = email_accessor
        self.reservation_accessor = reservation_accessor
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")

    def send_email(self, provider_spec: SendEmailProviderSpec) -> None:
        try:
            email_data = self.email_accessor.get_email_by_id(
                accessor_spec=GetEmailByIdAccessorSpec(
                    email_id=provider_spec.email_id
                )
            )
            reserved_email_addresses = self.reservation_accessor.get_reservation_emails_by_event_id(
                accessor_spec=GetReservationEmailsByEventIdAccessorSpec(
                    event_id=email_data.event_id
                )
            ).user_email_addresses
            msg = EmailMessage()
            msg['From'] = email_data.created_by
            msg['Subject'] = email_data.subject
            msg.set_content(email_data.content)
            with smtplib.SMTP(host=self.smtp_host, port=int(self.smtp_port)) as server:
                login_result = server.login(user=self.smtp_user, password=self.smtp_password)
                if login_result[0] not in [235, 503]:
                    raise smtplib.SMTPAuthenticationError(msg="Authentication fail.", code=535)
                for email in reserved_email_addresses:
                    msg['To'] = email
                    server.send_message(msg=msg)
        except smtplib.SMTPException:
            pass
