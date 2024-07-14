from typing import Dict, List

from pydantic import BaseModel, json

from app.direction.schemas import SDirection
from app.feedback.schemas import SFeedback, SFeedback2


class SProjectImage(BaseModel):
    photo_url: str
    result: bool

    class Config:
        from_attributes = True


class SProject(BaseModel):
    id: int
    name: Dict[str, str]
    title: Dict[str, str]
    description: Dict[str, str]
    category_id: int
    link: str
    feedback_id: int | None
    feedback: SFeedback2 | None
    images: List[SProjectImage]

    class Config:
        from_attributes = True


class SProjects(BaseModel):
    id: int
    name: Dict[str, str]
    title: Dict[str, str]
    description: Dict[str, str]
    category_id: int
    direction: SDirection
    link: str
    images: List[SProjectImage]

    class Config:
        from_attributes = True
