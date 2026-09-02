from app.database import SessionLocal
from app.models import Trip

db = SessionLocal()

trips = db.query(Trip).all()

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

db.close()