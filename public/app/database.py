from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import logging

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://pgadmin:secret@localhost:5432/formbricks')

# echo=True for debugging; keep False normally
engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

Base = declarative_base()

def init_db():
    # import models here to ensure they are registered on the metadata
    from . import models  # noqa: F401
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        # Don't let DB initialization failures crash the whole process in serverless environments.
        # Surface a clear log message so deploy logs can show the root cause.
        logging.exception('Failed to initialize database schema: %s', e)
        return False
    return True
