from typing import Dict

from pydantic import BaseModel


class SFeature(BaseModel):
    title: Dict[str, str]
    description: Dict[str, str]

    class Config:
        from_attributes = True
