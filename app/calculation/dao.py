from app.dao.base import BaseDAO
from app.calculation.model import Calculation


class CalculationDAO(BaseDAO):
    model = Calculation
