from typing import Dict, Union, List

from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.technology.dao import TechnologyDAO
from app.technology.schemas import STechnology

router = APIRouter(
    prefix="/technologies",
    tags=["Технологии"]
)


@router.get("")
@cache(expire=3600)
async def get_technologies() -> Dict[str, Union[str, List[STechnology]]]:
    technologies = await TechnologyDAO.get_all()

    return {"detail": "Все записи", "result": technologies}
