from app.database import SessionLocal
from app.models import UserProfile as DBUserProfile


class UserProfile:

    def __init__(self):

        db = SessionLocal()

        profile = db.query(
            DBUserProfile
        ).first()

        db.close()

        if profile:

            self.preferences = {

                "walking_level":
                    profile.walking_level,

                "hotel_type":
                    profile.hotel_preference,

                "budget":
                    profile.budget
            }

        else:

            self.preferences = {

                "walking_level":
                    "low",

                "hotel_type":
                    "city center",

                "budget":
                    "moderate"
            }