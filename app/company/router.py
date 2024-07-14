from typing import Dict, Union, Any

from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache
from typing_extensions import List

from app.company.dao import CompanyDAO
from app.company.schemas import SCompany

router = APIRouter(
    prefix="/company",
    tags=["Компании"]
)


@router.get("")
@cache(expire=20)
async def get_companies() -> Dict[str, Union[str, List[SCompany]]]:
    companies = await CompanyDAO.get_all()

    return {"detail": "Все записи", "result": companies}