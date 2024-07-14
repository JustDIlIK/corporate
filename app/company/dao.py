from sqlalchemy import select

from app.dao.base import BaseDAO
from app.company.model import Company
from app.database import async_session_maker


class CompanyDAO(BaseDAO):
    model = Company


