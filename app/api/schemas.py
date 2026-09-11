from pydantic import BaseModel


class TripCreate(BaseModel):
    origin: str
    destination: str
    days: int