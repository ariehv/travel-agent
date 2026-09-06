from app.ai_agent import AIAgent
from app.storage import save_trip
from app.user_profile import UserProfile


class TravelPlanner:

    def __init__(self):
        
        self.profile = UserProfile()
        self.ai = AIAgent()

    def generate_itinerary(self, origin, destination, days):    

        prompt = f"""
        Walking level:
        {self.profile.preferences['walking_level']}

        Hotel preference:
        {self.profile.preferences['hotel_type']}

        Budget:
        {self.profile.preferences['budget']}
        
        Create a {days}-day travel itinerary.

        Origin: {origin}
        Destination: {destination}

        Include:

        - hotels area suggestions
        - transportation
        - food
        - attractions
        - daily itinerary
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