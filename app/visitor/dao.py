from app.dao.base import BaseDAO
from app.visitor.model import Visitor


class VisitorDAO(BaseDAO):
    model = Visitor
