from pydantic import BaseModel


class TripCreate(BaseModel):
    origin: str
    destination: str
    days: int



class TripUpdate(BaseModel):
    origin: str | None = None
    destination: str | None = None
    days: int | None = None


class ProfileResponse(BaseModel):
    name: str
    home_airport: str
    budget: str
    walking_level: str
    hotel_type: str

class ProfileUpdate(BaseModel):
    name: str | None = None
    home_airport: str | None = None
    budget: str | None = None
    walking_level: str | None = None
    hotel_type: str | None = None