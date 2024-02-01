from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class BaseSqlaRepository:
    def __init__(self, db=None, connection_data=None):
        self.Base = NotImplemented
        self.db = db
        if not db:
            db_user = connection_data.get("user")
            db_password = connection_data.get("password")
            db_host = connection_data.get("host")
            db_port = connection_data.get("port")
            db_database = connection_data.get("database")

            dsn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
            self.engine = create_engine(dsn, poolclass=NullPool)
            self.Base.metadata.bind = self.engine

    @property
    def session_context(self):
        if self.db:
            @contextmanager
            def session_scope():
                yield self.db.session

        else:
            @contextmanager
            def session_scope():
                session_local = sessionmaker(bind=self.engine)
                session = session_local()
                try:
                    yield session
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        return session_scope