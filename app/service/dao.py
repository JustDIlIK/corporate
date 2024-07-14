from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.service.model import Service


class ServiceDAO(BaseDAO):
    model = Service

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.calculation))
            result = await session.execute(query)
            return result.scalars().all()