from sqlalchemy import select
from sqlalchemy.orm import joinedload, join, outerjoin, contains_eager, aliased

from app.client.model import Client
from app.company.model import Company
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.direction.model import Direction
from app.feedback.model import Feedback
from app.project.model import Project, ProjectImage


class ProjectDAO(BaseDAO):
    model = Project

    @classmethod
    async def get_all(cls):
        project_image_alias = aliased(ProjectImage)
        async with async_session_maker() as session:
            query = select(cls.model)\
            .options(joinedload(cls.model.images))\
            .options(joinedload(cls.model.feedback).joinedload(Feedback.client))\
            .options(joinedload(cls.model.direction))\
            .join(project_image_alias, cls.model.images)\
            .order_by(cls.model.id)

            result = await session.execute(query)
            return result.unique().scalars().all()

    @classmethod
    async def find_by_id(cls, record_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=record_id)\
                .options(joinedload(cls.model.feedback).joinedload(Feedback.client))\
                .options(joinedload(cls.model.images))
            result = await session.execute(query)
            return result.scalar()