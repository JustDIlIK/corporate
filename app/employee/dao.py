from app.dao.base import BaseDAO
from app.employee.model import Employee


class EmployeeDAO(BaseDAO):
    model = Employee