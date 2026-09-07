from app.database import SessionLocal
from app.models import UserProfile

db = SessionLocal()

profile = db.query(UserProfile).first()

if profile:

    print()
    print("Traveler Profile")
    print("-" * 40)

    print(f"ID: {profile.id}")
    print(f"Name: {profile.name}")
    print(f"Home Airport: {profile.home_airport}")
    print(f"Budget: {profile.budget}")
    print(f"Walking Level: {profile.walking_level}")
    print(f"Hotel Preference: {profile.hotel_preference}")

else:

    print("No profile found")

db.close()