from typing import Dict

from pydantic import BaseModel, json


class SAchievement(BaseModel):
    description: Dict[str, str]
    value: int

    class Config:
        from_attributes = True

