from app.travel_planner import TravelPlanner

planner = TravelPlanner()

destination = input(
    "Destination: "
)

days = input(
    "Days: "
)

result = planner.create_trip(
    "Tel Aviv",
    destination,
    days
)

print()
print(result)