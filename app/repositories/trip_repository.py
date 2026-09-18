from app.database import SessionLocal
from app.models import Trip
from sqlalchemy import or_
from collections import Counter

def save_trip(
    origin,
    destination,
    days,
    prompt,
    itinerary,
    food_guide,
    packing_list,
    hidden_gems,
    emergency_plan,
    optimized_itinerary
):

    db = SessionLocal()

    trip = Trip(
    origin=origin,
    destination=destination,
    days=days,
    prompt=prompt,
    itinerary=itinerary,
    food_guide=food_guide,
    packing_list=packing_list,
    hidden_gems=hidden_gems,
    emergency_plan=emergency_plan,
    optimized_itinerary=optimized_itinerary
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
    itinerary=None,
    food_guide=None,
    packing_list=None,
    hidden_gems=None,
    emergency_plan=None,
    optimized_itinerary=None
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

    if food_guide is not None:
        trip.food_guide = food_guide

    if packing_list is not None:
        trip.packing_list = packing_list

    if hidden_gems is not None:
        trip.hidden_gems = hidden_gems

    if emergency_plan is not None:
        trip.emergency_plan = emergency_plan

    if optimized_itinerary is not None:
        trip.optimized_itinerary = optimized_itinerary

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

def get_visited_destinations():

    db = SessionLocal()

    trips = db.query(Trip).all()

    destinations = [
        trip.destination
        for trip in trips
    ]

    db.close()

    return destinations