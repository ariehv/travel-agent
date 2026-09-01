# Travel Agent

## Requirements

- Python 3.12+
- Ollama

## Install Ollama

```bash
brew install ollama
```

## Download model

```bash
ollama pull qwen3:8b
```

## Run tests

```bash
python test_ollama.py
```


## Project Structure

```
── README.md
├── __pycache__
├── app
│   ├── __pycache__
│   │   ├── ai_agent.cpython-312.pyc
│   │   ├── database.cpython-312.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── models.cpython-312.pyc
│   │   ├── travel_planner.cpython-312.pyc
│   │   └── user_profile.cpython-312.pyc
│   ├── agents
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── budget_agent.py
│   │   ├── flight_agent.py
│   │   ├── hotel_agent.py
│   │   └── itinenary_agent.py
│   ├── ai_agent.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── travel_planner.py
│   └── user_profile.py
├── create_db.py
├── data
│   └── travel.db
├── docs
├── requirements.txt
├── run_agent.py
├── test.py
├── test_ai.py
├── test_ollama.py
├── test_trip.py
└── tests
```