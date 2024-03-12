import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv

from app.db.models import Base

load_dotenv()

USER = os.environ.get('PG_USER')
PASSWORD = os.environ.get('PG_PASSWORD')
HOST = os.environ.get('PG_HOST')
PORT = os.environ.get('PG_PORT')
NAME = os.environ.get('PG_NAME')


engine = create_async_engine(
    f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}',
    echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
