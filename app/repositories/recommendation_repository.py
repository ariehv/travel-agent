from app.repositories.trip_repository import (
    get_visited_destinations
)

from app.user_profile import UserProfile
from app.agents.recommendation_agent import (
    RecommendationAgent
)


def get_recommendations():

    profile = UserProfile()

    previous_destinations = (
        get_visited_destinations()
    )

    agent = RecommendationAgent()

    return agent.recommend(
        budget=profile.preferences["budget"],
        walking_level=profile.preferences["walking_level"],
        previous_destinations=previous_destinations
    )