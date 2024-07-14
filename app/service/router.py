from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.service.dao import ServiceDAO
from app.service.schemas import SService

router = APIRouter(
    prefix="/services",
    tags=["Услуги"]
)


@router.get("")
@cache(expire=3600)
async def get_services():
    services = await ServiceDAO.get_all()

    return {"detail": "Все записи", "result": services}
