from typing import Dict, Union, List

from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.client.schemas import SClient
from app.feedback.dao import FeedbackDAO
from app.feedback.schemas import SFeedback

router = APIRouter(
    prefix="/feedbacks",
    tags=["Отзывы"]
)


@router.get("")
@cache(expire=3600)
async def get_feedbacks() -> Dict[str, Union[str, List[SFeedback]]]:
    feedbacks = await FeedbackDAO.get_all()

    return {"detail": "Все записи", "result": feedbacks}
