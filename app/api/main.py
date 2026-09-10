from fastapi import FastAPI, HTTPException

from app.repositories.trip_repository import (
    list_trips,
    get_trip
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