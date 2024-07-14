from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.feature.dao import FeatureDAO
from app.feature.schemas import SFeature

router = APIRouter(
    prefix="/features",
    tags=["Возможности"]
)


@router.get("")
@cache(expire=3600)
async def get_features():
    features = await FeatureDAO.get_all()

    return {"detail": "Все записи", "result": features}

