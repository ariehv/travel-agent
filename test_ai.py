from app.ai_agent import AIAgent

agent = AIAgent()

answer = agent.ask(
    "Plan a 3-day trip to Athens"
)

print(answer)