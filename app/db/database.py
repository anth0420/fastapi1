from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings



SQLALCHEMY_DATABASE_URL = settings.DATBASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sesionlocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base = declarative_base()


def get_db():
    db = Sesionlocal()
    try:
        yield db
    finally:
        db.close()