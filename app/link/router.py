from typing import Dict, Union, List

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.link.dao import LinkDAO
from app.link.schemas import SLink

router = APIRouter(
    prefix="/links",
    tags=["Соц. сети"]
)


@router.get("")
@cache(expire=3600)
async def get_all() -> Dict[str, Union[str, List[SLink]]]:
    links = await LinkDAO.get_all()
    return {"detail": "Все записи", "result": links}

