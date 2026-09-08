from app.database import SessionLocal
from app.models import Trip


def save_trip(origin, destination, days,prompt, itinerary):

    db = SessionLocal()

    trip = Trip(
        origin=origin,
        destination=destination,
        days=days,
        prompt=prompt,
        itinerary=itinerary
    )

    db.add(trip)
    db.commit()

    db.refresh(trip)

    db.close()

    return trip.id

def get_trip(trip_id):

    db = SessionLocal()

    trip = db.query(Trip).filter(
        Trip.id == trip_id
    ).first()

    db.close()

    return trip