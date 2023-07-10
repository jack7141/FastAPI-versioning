import json
import os
from functools import lru_cache

from pydantic import BaseSettings

from common.utils import DotDict

secret_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'secrets.json')

with open(secret_file, encoding='utf-8') as f:
    secrets = DotDict(json.loads(f.read()))

def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    return secrets.get(setting)


DATABASE = get_secret('LOCAL')


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


class DevelopmentSettings(ISettings):
    pass


class ProductionSettings(ISettings):
    debug = False


@lru_cache()
def get_settings():
    config = os.environ.get("FASTAPI_CONFIG", 'default')
    configs = {
        "development": DevelopmentSettings,
        "production": ProductionSettings,
        "default": DevelopmentSettings
    }

    return configs.get(config, DevelopmentSettings)()
