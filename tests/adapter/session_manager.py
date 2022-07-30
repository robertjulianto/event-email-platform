from contextlib import contextmanager
from typing import ContextManager, no_type_check

from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, make_transient

from event_email.infrastructure.sqlalchemy.port import ISessionManager


class FakeSessionManager(ISessionManager):

    @inject
    def __init__(
            self):
        self.DB_NAME = 'event_email_unittest'
        self.engine = create_engine(f'postgresql://postgres:postgrespassword@localhost/{self.DB_NAME}')
        self.connection = self.engine.connect()
        self.transaction = self.connection.begin()
        self.session = sessionmaker()(bind=self.connection)

    def get_session_scope(self) -> ContextManager[Session]:
        @no_type_check
        @contextmanager
        def test_session_scope() -> ContextManager[Session]:
            session = self.session
            try:
                yield session
                # make all objects inside this session transient
                instances = session.identity_map.values() + list(session.new)
                for instance in instances:
                    make_transient(instance)
            except Exception as e:
                session.rollback()
                raise e

        return test_session_scope()

    def tear_down(self):
        self.session.close()
        self.connection.close()
        self.engine.dispose()
