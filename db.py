from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker
from app.config import settings

async_engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    # create tables if running without alembic (dev convenience)
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
