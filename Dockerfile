FROM python:3.8.8-buster
RUN pip install pipenv
WORKDIR /code
COPY Pipfile* ./
RUN pipenv install --deploy --system --ignore-pipfile
COPY event_email event_email
ENV PYTHONPATH="event_email:${PYTHONPATH}"
