from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config

engine = create_engine(config.dbconn, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def db_startup():
    pass

async def db_shutdown():
    pass