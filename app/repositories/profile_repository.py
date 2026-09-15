from app.database import SessionLocal
from app.models import UserProfile


def get_profile():

    db = SessionLocal()

    profile = db.query(
        UserProfile
    ).first()

    db.close()

    return profile

def update_profile(
    name=None,
    home_airport=None,
    budget=None,
    walking_level=None,
    hotel_preference=None
):

    db = SessionLocal()

    profile = db.query(
        UserProfile
    ).first()

    if not profile:

        db.close()
        return None

    if name is not None:
        profile.name = name

    if home_airport is not None:
        profile.home_airport = home_airport

    if budget is not None:
        profile.budget = budget

    if walking_level is not None:
        profile.walking_level = walking_level

    if hotel_preference is not None:
        profile.hotel_preference = hotel_preference

    db.commit()
    db.refresh(profile)

    db.close()

    return profile
