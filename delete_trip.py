

from app.repositories.trip_repository import delete_trip

trip_id = int(input("Trip ID to delete: "))

trip = delete_trip(trip_id
)
print("Trip deleted successfully")


