from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.achievement.dao import AchievementDAO
from app.achievement.schemas import SAchievement

router = APIRouter(
    prefix="/achievement",
    tags=["Достижения"]
)


@router.get("")
@cache(expire=3600)
async def get_achievements():
    achievements = await AchievementDAO.get_all()

    return {"detail": "Все записи", "result": achievements}

