from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings_get



SQLALCHEMY_DATABASE_GET = settings_get.DATABASE_GET

engine_get = create_engine(SQLALCHEMY_DATABASE_GET)
Sesionlocal = sessionmaker(bind=engine_get,autocommit=False,autoflush=False)

Base_get = declarative_base()


def get_db2():
    db = Sesionlocal()
    try:
        yield db
    finally:
        db.close()
