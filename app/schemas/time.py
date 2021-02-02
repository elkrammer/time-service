from pydantic import BaseModel


class Time(BaseModel):
    message: str
    timestamp: int
