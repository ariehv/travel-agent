from fastapi import FastAPI, HTTPException
from app.api.schemas import TripCreate
from app.travel_planner import TravelPlanner
from app.repositories.trip_repository import (
    list_trips,
    get_trip,
    delete_trip,
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