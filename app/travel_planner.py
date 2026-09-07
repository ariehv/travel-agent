from app.ai_agent import AIAgent
from app.storage import save_trip
from app.user_profile import UserProfile


class TravelPlanner:

    def __init__(self):
        
        self.profile = UserProfile()
        self.ai = AIAgent()

    def generate_itinerary(self, origin, destination, days):    
        prompt = f"""
        You are an experienced travel planner.

        Traveler Profile:

        Walking level:
        {self.profile.preferences['walking_level']}

        Hotel preference:
        {self.profile.preferences['hotel_type']}

        Budget:
        {self.profile.preferences['budget']}

        Trip Information:

        Origin:
        {origin}

        Destination:
        {destination}

        Duration:
        {days} days

        Create a detailed day-by-day itinerary.

        For each day include:

        - Morning activities
        - Afternoon activities
        - Evening activities
        - Recommended local food
        - Transportation tips

        Also include:

        1. Best hotel areas to stay in the destination
        2. Why each area is recommended based on the traveler's profile
        3.Flight recommendations if relevant
        4. Airport transfer instructions
        5. Public transportation advice
        6. Estimated daily budget
        7. Top attractions not to miss
        8. Local foods to try
        9. Safety tips
        10. Weather considerations if relevant

        Format the response clearly using:

        Day 1
        Day 2
        Day 3
        ...

        Be practical and realistic.
        """

        itinerary = self.ai.ask(prompt)
        
        return itinerary
    
    def create_trip(
        self,
        origin,
        destination,
        days
    ):

        
        itinerary = self.generate_itinerary(origin, destination, days)
        

        trip_id = save_trip(
            origin,
            destination,
            days,
            itinerary
        )

        print(f"Trip saved with ID {trip_id}")

        return itinerary