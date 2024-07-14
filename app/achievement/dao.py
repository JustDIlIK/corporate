from app.dao.base import BaseDAO
from app.achievement.model import Achievement


class AchievementDAO(BaseDAO):
    model = Achievement