from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.client.model import Client
from app.database import async_session_maker


class ClientDAO(BaseDAO):
    model = Client

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.company))
            result = await session.execute(query)

            return result.scalars().all()