from datetime import datetime

from sqlalchemy import update, select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.statistic.model import Statistic


class StatisticDAO(BaseDAO):
    model = Statistic

    @classmethod
    async def update_count(cls, date):
        async with async_session_maker() as session:      
            record = await cls.find_one_or_none(statistic_date=date)
            if not record:
                return await cls.add_record(count=1, statistic_date=date)

            query = update(cls.model).filter_by(statistic_date=date).values(count=cls.model.count + 1).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

    @classmethod
    async def get_statistic_by_day(cls, **day):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**day)
            result = await session.execute(query)
            return result.scalars().first()