from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings
from sqlalchemy import  create_engine

DATABASE_URL = settings.DATABASE_URL

#creat async engine
engine = create_engine(DATABASE_URL)

#creat session factory
SessionLocal = sessionmaker(
   autocommit=False,
    autoflush=False,
    bind=engine
)

#base class for models
class Base(DeclarativeBase):
    pass

#database sessiion per request
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()