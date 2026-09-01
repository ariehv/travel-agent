from app.travel_planner import TravelPlanner

planner = TravelPlanner()

trip = planner.create_trip(
    "Tel Aviv",
    "Vilnius",
    7
)

print(trip)