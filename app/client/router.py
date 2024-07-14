from typing import Dict, Union, List

from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.client.dao import ClientDAO
from app.client.schemas import SClient

router = APIRouter(
    prefix="/client",
    tags=["Клиенты"]
)


@router.get("")
@cache(expire=20)
async def get_clients() -> Dict[str, Union[str, List[SClient]]]:
    clients = await ClientDAO.get_all()

    return {"detail": "Все записи", "result": clients}
