from typing import Dict

from pydantic import BaseModel


class SLang(BaseModel):
    lang_short: Dict[str, str]
    lang_long: Dict[str, str]

    class Config:
        from_attributes = True
