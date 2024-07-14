from typing import Dict

from pydantic import BaseModel


class SDirection(BaseModel):
    content: Dict[str, str]

    class Config:
        from_attributes = True

