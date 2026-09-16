from app.database import SessionLocal
from app.models import Trip
from sqlalchemy import or_
from collections import Counter

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
                f"{trip.origin} -> "
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

    if not trip:

        db.close()

        return False

    db.delete(trip)

    db.commit()

    db.close()

    return True


def update_trip(trip_id):
    from app.travel_planner import TravelPlanner
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

    prompt, new_itinerary = TravelPlanner().generate_itinerary(
    trip.origin,
    trip.destination,
    trip.days
)
    trip.prompt = prompt
    trip.itinerary = new_itinerary
    db.commit()
    
    print()
    print("Trip updated successfully")

    db.close()

def get_trip_history():

    db = SessionLocal()

    trips = db.query(Trip).all()

    db.close()

    return trips

def update_trip_data(
    trip_id,
    origin=None,
    destination=None,
    days=None,
    prompt=None,
    itinerary=None
):
    db = SessionLocal()

    trip = db.query(Trip).filter(
        Trip.id == trip_id
    ).first()

    if not trip:
        db.close()
        return None

    if origin is not None:
        trip.origin = origin

    if destination is not None:
        trip.destination = destination

    if days is not None:
        trip.days = days

    if prompt is not None:
        trip.prompt = prompt

    if itinerary is not None:
        trip.itinerary = itinerary

    db.commit()
    db.refresh(trip)

    db.close()

    return trip

def get_trip_stats():

    db = SessionLocal()

    trips = db.query(Trip).all()

    total_trips = len(trips)

    total_days = sum(
        trip.days for trip in trips
    )
    destination_counts = Counter(
    trip.destination
    for trip in trips
    )

    top_destinations = [
        destination
        for destination, count
        in destination_counts.most_common(3)
    ]
    
    average_trip_days = (
        total_days / total_trips
            if total_trips > 0
            else 0
        )
    db.close()

    return {
    "total_trips": total_trips,
    "total_days": total_days,
    "average_trip_days": round(
        average_trip_days,
        1
    ),
    "top_destinations": top_destinations
    }   