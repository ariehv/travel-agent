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

    itinerary = Column(Text)