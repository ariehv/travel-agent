from app.database import SessionLocal
from app.models import UserProfile

db = SessionLocal()

profile = UserProfile(
    name="Lenia",
    home_airport="TLV",
    budget="Moderate",
    walking_level="Low",
    hotel_preference="City Center"
)

db.add(profile)

db.commit()

db.refresh(profile)

print(f"Profile created with ID {profile.id}")

db.close()