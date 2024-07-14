from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.feedback.model import Feedback


class FeedbackDAO(BaseDAO):
    model = Feedback

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(cls.model.client))
            result = await session.execute(query)

            return result.scalars().all()
