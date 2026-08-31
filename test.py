from app.agents.budget_agent import BudgetAgent
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.itinenary_agent import ItineraryAgent

flight = FlightAgent()
hotel = HotelAgent()
budget = BudgetAgent()
itinenary = ItineraryAgent()


print(flight.search("TLV", "Buenos Aires"))
print()

print(hotel.search("Buenos Aires"))
print()

print(budget.calculate())
print()

print(itinenary.build())