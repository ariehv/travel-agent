from app.agents.flight_agent import FlightAgent

print("Travel Agent Started")
print()

agent = FlightAgent()

trip = agent.search(
    "TLV",
    "Buenos Aires"
)

print("Trip Request:")
print(f"From: {trip['origin']}")
print(f"To: {trip['destination']}")
print()

print("Suggested Route:")
print(trip["route"])