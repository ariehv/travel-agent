from app.agents.flight_agent import FlightAgent

agent = FlightAgent()

print(
    agent.search(
        "TLV",
        "EZE"
    )
)