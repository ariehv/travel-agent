from app.ai_agent import AIAgent
from app.repositories.trip_repository import get_trip_history, save_trip
from app.user_profile import UserProfile
from app.repositories.trip_repository import (
    get_trip,
    update_trip_data
)
from app.agents.hotel_agent import HotelAgent
from app.agents.flight_agent import FlightAgent

class TravelPlanner:

    def __init__(self):
        
        self.profile = UserProfile()
        self.ai = AIAgent()
        self.hotel_agent = HotelAgent()
        self.flight_agent = FlightAgent()

    def get_trip_history(self):
    
        from app.database import SessionLocal
        from app.models import Trip
    
        db = SessionLocal()
    
        trips = db.query(Trip).all()
    
        db.close()
    
        return trips
    

    def generate_itinerary(self, origin, destination, days): 

        history = get_trip_history() 
        history_text = ""

        for trip in history:

            history_text += (
            f"- {trip.destination}\n"
            f"({trip.days} days)\n"
    ) 

        hotel_info = self.hotel_agent.search(
            destination
    )
        flight_info = self.flight_agent.search(
            origin,
            destination
    )

        
        prompt = f"""
        You are an experienced travel planner.
        Previous trips:
        {history_text}

        Hotel Recommendation:
        Hotel: {hotel_info['hotel']}
        Price: ${hotel_info['price']}

        Flight Recommendation:
        Route: {flight_info['route']}
        The traveler has already visited
        the destinations listed above.

        Avoid repeating the same generic
        recommendations.
        Traveler Profile:
        Name: {self.profile.preferences['name']}
        Home Airport: {self.profile.preferences['home_airport']}

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
        print("\nPROMPT SENT TO AI")
        print("-" * 40)
        print(prompt)
        print("-" * 40)

        itinerary = self.ai.ask(prompt)
        
        return prompt,itinerary
    
    def create_trip(
        self,
        origin,
        destination,
        days
    ):

        
        prompt, itinerary = self.generate_itinerary(origin, destination, days)
        

        trip_id = save_trip(
            origin,
            destination,
            days,
            prompt,
            itinerary
        )

        print(f"Trip saved with ID {trip_id}")

        return itinerary

    def update_trip(
        self,
        trip_id,
        origin=None,
        destination=None,
        days=None
    ):

        trip = get_trip(trip_id)

        if not trip:
            return None

        origin = origin or trip.origin
        destination = destination or trip.destination
        days = days or trip.days

        prompt, itinerary = self.generate_itinerary(
            origin,
            destination,
            days
            )

        return update_trip_data(
            trip_id,
            origin=origin,
            destination=destination,
            days=days,
            prompt=prompt,
            itinerary=itinerary
        )