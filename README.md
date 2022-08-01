# Event Email Scheduling API

## Functional Requirement

This system is used for covering cases for scheduling email sending based.

Before begin, you need to have these tools installed

* [Docker](https://www.docker.com/)
* [Postgres Docker image](https://hub.docker.com/_/postgres)
* [Liquibase Docker image](https://hub.docker.com/r/liquibase/liquibase)
* [RabbitMQ Docker image](https://hub.docker.com/_/rabbitmq)
* [Python](https://www.python.org/) (recommended to use [pyenv](https://github.com/pyenv/pyenv))
* [Pipenv](https://github.com/pypa/pipenv)

#### Postgres

* User `postgres`
* Password `postgrespassword`
* Port `5432`
* Container name `event_email_postgres`

#### RabbitMQ

* User `rabbitmq`
* Password `rabbitmqpassword`
* Port `5672`, `15672`
* Container name `event_email_rabbit`

## Migrations

This project is using Liquibase, read more about it [here](https://www.liquibase.org/). To run the liquibase and see all
the options, run this command:

```bash
./scripts/liquibase.sh --help
```

## Preparation

1. Open terminal into your project directory and install library using pipenv command

```bash
pipenv install
```

2. Activate virtual environment

```bash
pipenv shell
```
3. Create and start container

```bash
docker compose up -d
```

4. Access container event_email_postgres

```bash
docker exec -it event_email_postgres bash
```

5. Go into postgres instance and access database `event_email`

```bash
psql -U postgres -d event_email
```

6. Create schema `event_email`

```sql
CREATE SCHEMA event_email;
```

7. Quit from postgres instance
```bash
\q
```
then
```bash
exit
```

8. Still in your project directory, run migration for container

```bash
./scripts/liquibase.sh -e container -s
```


## Developer Test

This project is using classical approach. We are using:

1. [pytest](https://docs.pytest.org/)
2. [pytest-bdd](https://pytest-bdd.readthedocs.io/en/latest/)
3. [Postgres Docker image](https://hub.docker.com/_/postgres)

Execute the step below to run our classical test:

1. Create database `balance_unittest` and schema `balance` on your local postgres container.

2. Go to your project directory and run migration.
```bash
./scripts/liquibase.sh -e unittest
```

3. Run the tests.

```
pytest tests
```

nb: You'll also need to do this everytime there's new migration. Don't do anything to the database including insert,
update, and delete data.

## Development Tools
### MyPy

Install development dependencies and use mypy to check type annotations with command below:

```bash
dmypy run -- --namespace-packages --ignore-missing-imports .
```

or simply:

```bash
mypy .
```