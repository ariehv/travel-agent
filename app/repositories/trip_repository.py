from app.database import SessionLocal
from app.models import Trip
from sqlalchemy import or_
from app.travel_planner import TravelPlanner

def save_trip(
    origin,
    destination,
    days,
    itinerary
):

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
def get_trip(trip_id):

    db = SessionLocal()

    trip = db.query(Trip).filter(
        Trip.id == trip_id
    ).first()

    db.close()

    return trip
def list_trips():

    db = SessionLocal()

    trips = db.query(Trip).all()

    db.close()

    return trips

    



def search_trips(search_text):
    db = SessionLocal()

    if not search_text:

        print("Search text cannot be empty")
        db.close()
        exit()

    trips = db.query(Trip).filter(
        or_(
            Trip.destination.ilike(f"%{search_text}%"),
            Trip.origin.ilike(f"%{search_text}%")
        )

    ).all()

    print()
    print("Results")
    print("-" * 40)

    if trips:

        for trip in trips:

            print(
                f"{trip.id} | "
                f"{trip.destination} | "
                f"{trip.days} days"
            )

    else:

        print("No trips found")

    db.close()
    return trips

def delete_trip(trip_id):

    db = SessionLocal()

    trip = db.query(Trip).filter(
        Trip.id == trip_id
    ).first()

    if trip:

        db.delete(trip)

        db.commit()

    db.close()

def update_trip(trip_id):

    db = SessionLocal()

    trip = db.query(Trip).filter(
        Trip.id == trip_id
    ).first()

    if not trip:

        print("Trip not found")

        db.close()

        exit()

    print(f"Current origin: {trip.origin}  ")
    print(f"Current destination: {trip.destination}")
    print(f"Current days: {trip.days}")
    print()
    new_origin = input(
        "New origin (Enter to keep current): "
    ).strip()

    new_destination = input(
        "New destination (Enter to keep current): "
    ).strip()

    new_days = input(
        "New days (Enter to keep current): "
    ).strip()

    if new_destination:

        trip.destination = new_destination

    if new_days:

        trip.days = int(new_days)
    if new_origin:

        trip.origin = new_origin    
    new_itinerary =TravelPlanner().generate_itinerary(trip.origin, trip.destination, trip.days)
    trip.itinerary = new_itinerary
    db.commit()
    
    print()
    print("Trip updated successfully")

    db.close()