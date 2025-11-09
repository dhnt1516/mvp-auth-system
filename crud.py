from sqlmodel import select
from app.models import User
from app.db import async_session
from sqlalchemy.exc import IntegrityError
from app.logger import logger

async def get_user_by_login(login: str):
    async with async_session() as session:
        result = await session.exec(select(User).where(User.login == login))
        return result.first()

async def create_user(login: str, password_hash: str):
    async with async_session() as session:
        user = User(login=login, password_hash=password_hash)
        session.add(user)
        try:
            await session.commit()
            await session.refresh(user)
            logger.info(f"User created: {login}")
            return user
        except IntegrityError as e:
            await session.rollback()
            logger.error(f"Integrity error while creating user {login}: {e}")
            raise
