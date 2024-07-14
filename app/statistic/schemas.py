from pydantic import BaseModel


class SStatistic(BaseModel):
    statistic_date: str

    class Config:
        from_attributes = True
