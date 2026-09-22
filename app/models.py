from datetime import datetime, timezone

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime, Integer, String, Text

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

    food_guide = Column(Text)
    
    packing_list = Column(Text)
    hidden_gems = Column(Text)
    emergency_plan= Column(Text)
    optimized_itinerary = Column(Text)
    weather_guide = Column(Text)
    currency_guide = Column(Text)
    visa_guide = Column(Text)
    transport_guide = Column(Text)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class UserProfile(Base):

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    home_airport = Column(String)

    budget = Column(String)

    walking_level = Column(String)

    hotel_preference = Column(String)

    