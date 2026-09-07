from app.database import SessionLocal
from app.models import UserProfile

db = SessionLocal()

profile = db.query(UserProfile).first()

if not profile:

    print("No profile found")

    db.close()

    exit()

print()
print("Current Profile")
print("-" * 40)

print(f"Name: {profile.name}")
print(f"Home Airport: {profile.home_airport}")
print(f"Budget: {profile.budget}")
print(f"Walking Level: {profile.walking_level}")
print(f"Hotel Preference: {profile.hotel_preference}")

print()

name = input(
    f"Name ({profile.name}): "
).strip()

home_airport = input(
    f"Home Airport ({profile.home_airport}): "
).strip()

budget = input(
    f"Budget ({profile.budget}): "
).strip()

walking_level = input(
    f"Walking Level ({profile.walking_level}): "
).strip()

hotel_preference = input(
    f"Hotel Preference ({profile.hotel_preference}): "
).strip()

if name:
    profile.name = name

if home_airport:
    profile.home_airport = home_airport

if budget:
    profile.budget = budget

if walking_level:
    profile.walking_level = walking_level

if hotel_preference:
    profile.hotel_preference = hotel_preference

db.commit()

print()
print("Profile updated")

db.close()