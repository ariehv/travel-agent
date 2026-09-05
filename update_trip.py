from app.repositories.trip_repository import update_trip

trip_id = int(input("Trip ID to update: "))
update_trip(trip_id)
