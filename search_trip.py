from app.repositories.trip_repository import search_trips

search_text = input("Destination or Origin: ").strip()

trips = search_trips(search_text)
