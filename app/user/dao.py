from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.user.models import User


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar()
