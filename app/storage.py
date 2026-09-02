from app.database import SessionLocal
from app.models import Trip


def save_trip(origin, destination, days, itinerary):

    db = SessionLocal()

    trip = Trip(
        origin=origin,
        destination=destination,
        days=days,
        itinerary=itinerary
    )

    db.add(trip)
    db.commit()

    db.refresh(trip)

    db.close()

    return trip.id