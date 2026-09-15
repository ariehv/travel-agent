from fastapi import FastAPI, HTTPException
from app.api.schemas import (
    TripCreate,
    TripUpdate,
    ProfileUpdate
)
from app.travel_planner import TravelPlanner
from app.repositories.trip_repository import (
    list_trips,
    get_trip,
    delete_trip,
    get_trip_stats
)
from app.repositories.profile_repository import (
    get_profile,
    update_profile
)
app = FastAPI(
    title="Travel Agent API"
)


@app.get("/")
def home():

    return {
        "message": "Travel Agent API Running"
    }


@app.get("/trips")
def get_trips():

    trips = list_trips()

    return [
        {
            "id": trip.id,
            "origin": trip.origin,
            "destination": trip.destination,
            "days": trip.days
        }
        for trip in trips
    ]


@app.get("/trips/{trip_id}")
def get_trip_by_id(trip_id: int):

    trip = get_trip(trip_id)

    if not trip:

        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return {
        "id": trip.id,
        "origin": trip.origin,
        "destination": trip.destination,
        "days": trip.days,
        "itinerary": trip.itinerary
    }
@app.post("/trips")
def create_trip(trip: TripCreate):

    planner = TravelPlanner()

    itinerary = planner.create_trip(
        origin=trip.origin,
        destination=trip.destination,
        days=trip.days
    )

    return {
        "origin": trip.origin,
        "destination": trip.destination,
        "days": trip.days,
        "itinerary": itinerary
    }



@app.delete("/trips/{trip_id}")
def delete_trip_endpoint(trip_id: int):

    deleted = delete_trip(trip_id)

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return {
        "message": f"Trip {trip_id} deleted successfully"
    }
@app.put("/trips/{trip_id}")
def update_trip_endpoint(
    trip_id: int,
    trip: TripUpdate
):

    planner = TravelPlanner()

    updated_trip = planner.update_trip(
        trip_id=trip_id,
        origin=trip.origin,
        destination=trip.destination,
        days=trip.days
    )

    if not updated_trip:

        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return {
        "id": updated_trip.id,
        "origin": updated_trip.origin,
        "destination": updated_trip.destination,
        "days": updated_trip.days,
        "itinerary": updated_trip.itinerary
    }

@app.get("/stats")
def stats():

    return get_trip_stats()

@app.get("/profile")
def profile():

    profile = get_profile()

    if not profile:

        return {
            "message": "No profile found"
        }

    return {
        "name": profile.name,
        "home_airport": profile.home_airport,
        "budget": profile.budget,
        "walking_level": profile.walking_level,
        "hotel_preference": profile.hotel_preference
    }

@app.put("/profile")
def update_profile_endpoint(
    profile: ProfileUpdate
):

    updated_profile = update_profile(
        name=profile.name,
        home_airport=profile.home_airport,
        budget=profile.budget,
        walking_level=profile.walking_level,
        hotel_preference=profile.hotel_type
    )

    if not updated_profile:

        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return {
        "name": updated_profile.name,
        "home_airport": updated_profile.home_airport,
        "budget": updated_profile.budget,
        "walking_level": updated_profile.walking_level,
        "hotel_preference": updated_profile.hotel_preference
    }