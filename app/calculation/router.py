from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.calculation.dao import CalculationDAO
from app.calculation.schemas import SCalculation

router = APIRouter(
    prefix="/calculations",
    tags=["Калькуляция"]
)


@router.get("")
@cache(expire=3600)
async def get_calculations():
    calculations = await CalculationDAO.get_all()

    return {"detail": "Все записи", "result": calculations}

