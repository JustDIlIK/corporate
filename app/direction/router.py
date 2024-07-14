from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.direction.dao import DirectionDAO
from app.direction.schemas import SDirection

router = APIRouter(
    prefix="/directions",
    tags=["Направления"]
)


@router.get("")
@cache(expire=3600)
async def get_directions():
    directions = await DirectionDAO.get_all()

    return {"detail": "Все записи", "result": directions}

