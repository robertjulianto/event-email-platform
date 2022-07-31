import os

from celery import Celery

from event_email.app.worker.di import injector
from event_email.core.common.port.logger import ILogger
from event_email.infrastructure.email.port.email_provider import IEmailProvider, SendEmailProviderSpec

app = Celery('main_task', broker=os.getenv('CELERY_BROKER_URL'))

logger = injector.get(ILogger)  # type: ignore
email_provider = injector.get(IEmailProvider)  # type: ignore


@app.task
def send_email(email_id: int):
    logger.info("Sending email....")
    email_provider.send_email(
        provider_spec=SendEmailProviderSpec(
            email_id=email_id
        )
    )
    logger.info("Sending email is done.")
