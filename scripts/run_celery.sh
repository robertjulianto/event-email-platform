export CELERY_BROKER_URL=amqp://rabbitmq:rabbitmqpassword@localhost:5672
export CELERY_SMTP_HOST=CELERY_SMTP_HOST
export CELERY_SMTP_PORT=CELERY_SMTP_PORT
export CELERY_SMTP_USER=CELERY_SMTP_USER
export CELERY_SMTP_PASSWORD=CELERY_SMTP_PASSWORD
export DB_HOST=localhost
celery -A event_email.app.worker.main_task worker --loglevel=info --pool=solo
