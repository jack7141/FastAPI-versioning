from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# 기존에 정의한 get_settings 함수를 import 합니다.
from conf.base import get_settings

DATABASE_URL = get_settings().db_dsn  # 설정 파일에서 dsn 정보를 가져옵니다.

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
