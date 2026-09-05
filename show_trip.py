
from app.repositories.trip_repository import get_trip

trip=get_trip(int(input("Trip ID: ")))


if trip:

    print("\n" + "=" * 50)
    print(f"Trip ID: {trip.id}")
    print(f"Origin: {trip.origin}")
    print(f"Destination: {trip.destination}")
    print(f"Days: {trip.days}")
    print("=" * 50)

    print("\nItinerary:\n")
    print(trip.itinerary)

else:

    print("Trip not found")

