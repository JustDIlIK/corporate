from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.lang.dao import LangDAO
from app.lang.schemas import SLang

router = APIRouter(
    prefix="/langs",
    tags=["Языки"]
)


@router.get("")
@cache(expire=3600)
async def get_langs():
    langs = await LangDAO.get_all()

    return {"detail": "Все записи", "result": langs}

