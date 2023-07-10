from base import *


DATABASE = get_secret('DEV')


class ISettings(BaseSettings):
    db_user: str = DATABASE.USER
    db_password: str = DATABASE.PASSWORD
    db_host: str = DATABASE.HOST
    db_port: int = DATABASE.PORT
    db_database: str = DATABASE.NAME

    debug: bool = True

    @property
    def db_dsn(self):
        dsn = f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_database}"
        return dsn