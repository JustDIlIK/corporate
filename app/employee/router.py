from typing import Dict, Union, List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.employee.dao import EmployeeDAO
from app.employee.schemas import SEmployee

router = APIRouter(
    prefix="/employees",
    tags=["Сотрудники"]
)


@router.get("")
@cache(expire=30)
async def get_employees() -> Dict[str, Union[str, List[SEmployee]]]:
    employees = await EmployeeDAO.get_all()


    return {"detail": "Все записи", "result": employees}
