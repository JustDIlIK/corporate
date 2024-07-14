from pydantic import BaseModel


class SLink(BaseModel):
    name: str
    url: str
    photo_url: str

    class Config:
        from_attributes = True


