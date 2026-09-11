from app.api.schemas import TripCreate


trip = TripCreate(
    origin="TLV",
    destination="Prague",
    days=5
)

print(trip)
print(trip.origin)
print(trip.destination)
print(trip.days)