
from app.repositories.trip_repository import list_trips 


trips = list_trips()

print()
print("Saved Trips")
print("-" * 40)

for trip in trips:

        print(
            f"{trip.id} | "
            f"{trip.origin} -> "
            f"{trip.destination} | "
            f"{trip.days} days"
        )