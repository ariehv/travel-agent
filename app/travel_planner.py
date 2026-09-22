from app.agents.packing_agent import PackingAgent
from app.agents.weather_agent import WeatherAgent
from app.ai_agent import AIAgent
from app.repositories.trip_repository import get_trip_history, save_trip
from app.user_profile import UserProfile
from app.repositories.trip_repository import (
    get_trip,
    update_trip_data
)
from app.agents.hotel_agent import HotelAgent
from app.agents.flight_agent import FlightAgent
from app.agents.budget_agent import BudgetAgent
from app.agents.hidden_gems_agent import HiddenGemsAgent
from app.agents.emergency_agent import EmergencyAgent
from app.agents.optimizer_agent import OptimizerAgent
from app.agents.food_agent import FoodAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.currency_agent import CurrencyAgent
from app.agents.visa_agent import VisaAgent
from app.agents.local_transport_agent import LocalTransportAgent


class TravelPlanner:

    def __init__(self):
        
        self.profile = UserProfile()
        self.ai = AIAgent()
        self.hotel_agent = HotelAgent()
        self.flight_agent = FlightAgent()
        self.budget_agent = BudgetAgent()
        self.packing_agent = PackingAgent()
        self.hidden_gems_agent = HiddenGemsAgent()
        self.emergency_agent = EmergencyAgent()
        self.optimizer_agent = OptimizerAgent()
        self.food_agent = FoodAgent()
        self.validation_agent = ValidationAgent()
        self.weather_agent = WeatherAgent()
        self.currency_agent = CurrencyAgent()
        self.visa_agent = VisaAgent()
        self.local_transport_agent = LocalTransportAgent()

        

    def get_trip_history(self):
    
        from app.database import SessionLocal
        from app.models import Trip
    
        db = SessionLocal()
    
        trips = db.query(Trip).all()
    
        db.close()
    
        return trips
    

    def generate_itinerary(self, origin, destination, days): 

        history = self.get_trip_history()
        history_text = ""

        for trip in history:

            history_text += (
            f"- {trip.destination}\n"
            f"({trip.days} days)\n"
    ) 

        
        
        budget_info = self.budget_agent.estimate(
            self.profile.preferences['budget'],
        )

        hotel_prompt = self.hotel_agent.build_prompt(
            destination
        )

        hotel_info = self.ai.ask(
            hotel_prompt
        )

        flight_prompt = self.flight_agent.build_prompt(
            origin,
            destination
        )

        flight_info = self.ai.ask(
            flight_prompt
        )
        food_prompt = self.food_agent.build_prompt(
            destination
        )
        food_guide = self.ai.ask(
            food_prompt
        )
        currency_prompt = self.currency_agent.build_prompt(
            destination
        )
        currency_guide = self.ai.ask(
            currency_prompt
        )
        visa_prompt = self.visa_agent.build_prompt(
            self.profile.origin,
            destination
        )
        visa_guide = self.ai.ask(
            visa_prompt
        )
        local_transport_prompt = self.local_transport_agent.build_prompt(
            destination
        )
        local_transport_guide = self.ai.ask(
            local_transport_prompt
        )       
        packing_prompt = self.packing_agent.build_prompt(
            destination,
            days
        )

        packing_list = self.ai.ask(
            packing_prompt
        )

        hidden_prompt = (
            self.hidden_gems_agent.build_prompt(
                destination
            )
        )

        hidden_gems = self.ai.ask(
            hidden_prompt
        )


        emergency_prompt = (
            self.emergency_agent.build_prompt(
                destination
        )
    )   

        emergency_plan = self.ai.ask(
            emergency_prompt
        )

        optimizer_prompt = (
            self.optimizer_agent.build_prompt(
                destination,
                days
        )
)

        optimized_itinerary = self.ai.ask(
             optimizer_prompt
)
        weather_prompt = (
            self.weather_agent.build_prompt(
                destination
            )
        )
        weather_guide = self.ai.ask(
            weather_prompt
        )

        print("\nPacking List:")
        print("-" * 40)
        print(packing_list)
        print("-" * 40)
        print("\nFood Guide:")
        print("-" * 40)
        print(food_guide)
        print("-" * 40) 
        print("\nHidden Gems:")
        print("-" * 40)
        print(hidden_gems)
        print("-" * 40) 
        print("\nEmergency Plan:")
        print("-" * 40)
        print(emergency_plan)
        print("-" * 40) 
        print("\nOptimized Itinerary:")
        print("-" * 40)
        print(optimized_itinerary)
        print("-" * 40) 
        print("\nWeather Guide:")   
        print("-" * 40)
        print(weather_guide)
        print("-" * 40) 
        print("\nCurrency Guide:")
        print("-" * 40)
        print(currency_guide)
        print("-" * 40)
        print("\nVisa Guide:")
        print("-" * 40)
        print(visa_guide)
        print("-" * 40)         
        print("\nLocal Transport Guide:")
        print("-" * 40)
        print(local_transport_guide)
        print("-" * 40)    



        prompt = f"""
        You are an experienced travel planner.
        Previous trips:
        {history_text}

        Hotel Recommendation:
        {hotel_info}

        Flight Recommendation:
        {flight_info}
        
        The traveler has already visited
        the destinations listed above.

        Avoid recommending attractions that
        appear in those previous itineraries.

        Prefer new experiences and different
        neighborhoods when possible.

        Take the travel history into account
        when creating recommendations.

        Traveler Profile:
        Name: {self.profile.preferences['name']}
        Home Airport: {self.profile.preferences['home_airport']}

        Walking level:
        {self.profile.preferences['walking_level']}

        Hotel preference:
        {self.profile.preferences['hotel_type']}

        Budget Recommendation:
        Expected Daily Spending: {budget_info}
        
    
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
        validation_prompt=(
            self.validation_agent.build_prompt(
                destination,
                itinerary
            )
        )
        validated_itinerary = self.ai.ask(validation_prompt)    
        itinerary = validated_itinerary
        
        return (
            prompt,
            itinerary,
            food_guide,
            packing_list,
            hidden_gems,
            emergency_plan,
            optimized_itinerary,
            weather_guide,
            currency_guide,
            visa_guide,
            local_transport_guide
        )
    def create_trip(
        self,
        origin,
        destination,
        days
    ):

        (
            prompt,
            itinerary,
            food_guide,
            packing_list,
            hidden_gems,
            emergency_plan,
            optimized_itinerary,
            weather_guide,
            currency_guide,
            visa_guide,
            local_transport_guide
        ) = self.generate_itinerary(
            origin,
            destination,
            days
        )

        trip_id = save_trip(
            origin,
            destination,
            days,
            prompt,
            itinerary,
            food_guide,
            packing_list,
            hidden_gems,
            emergency_plan,
            optimized_itinerary,
            weather_guide,
            currency_guide,
            visa_guide,
            local_transport_guide
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

        (
            prompt,
            itinerary,
            food_guide,
            packing_list,
            hidden_gems,
            emergency_plan,
            optimized_itinerary,
            weather_guide,
            currency_guide,
            visa_guide,
            local_transport_guide
        ) = self.generate_itinerary(
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
            itinerary=itinerary,
            food_guide=food_guide,
            packing_list=packing_list,
            hidden_gems=hidden_gems,
            emergency_plan=emergency_plan,
            optimized_itinerary=optimized_itinerary,
            weather_guide=weather_guide,
            currency_guide=currency_guide,
            visa_guide=visa_guide,
            local_transport_guide=local_transport_guide
        )