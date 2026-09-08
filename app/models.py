from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text

class Base(DeclarativeBase):
    pass


class Trip(Base):

    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)

    origin = Column(String)

    destination = Column(String)

    days = Column(Integer)
    prompt = Column(Text)

    itinerary = Column(Text)


class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    home_airport = Column(String)

    budget = Column(String)

    walking_level = Column(String)

    hotel_preference = Column(String)