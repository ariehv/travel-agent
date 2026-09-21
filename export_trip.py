from pathlib import Path

from app.repositories.trip_repository import get_trip


trip_id = int(input("Trip ID: "))

trip = get_trip(trip_id)

if not trip:

    print("Trip not found")
    exit()

# Create exports folder if it doesn't exist
Path("exports").mkdir(exist_ok=True)

filename = f"exports/trip_{trip.id}.txt"

with open(filename, "w", encoding="utf-8") as f:

    f.write("=" * 60 + "\n")
    f.write("TRIP INFORMATION\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Trip ID: {trip.id}\n")
    f.write(f"Origin: {trip.origin}\n")
    f.write(f"Destination: {trip.destination}\n")
    f.write(f"Days: {trip.days}\n\n")

    # Only if your Trip model contains prompt
    if hasattr(trip, "prompt") and trip.prompt:

        f.write("=" * 60 + "\n")
        f.write("PROMPT\n")
        f.write("=" * 60 + "\n\n")

        f.write(trip.prompt)
        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("ITINERARY\n")
        f.write("=" * 60 + "\n\n")

        f.write(trip.itinerary)

        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("FOOD GUIDE\n")
        f.write("=" * 60 + "\n\n")
        f.write(trip.food_guide or "")
        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("PACKING LIST\n")
        f.write("=" * 60 + "\n\n")
        f.write(trip.packing_list or "")
        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("HIDDEN GEMS\n")
        f.write("=" * 60 + "\n\n")
        f.write(trip.hidden_gems or "")
        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("EMERGENCY PLAN\n")
        f.write("=" * 60 + "\n\n")
        f.write(trip.emergency_plan or "")
        f.write("\n\n")

        f.write("=" * 60 + "\n")
        f.write("OPTIMIZED ITINERARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(trip.optimized_itinerary or "")

print()
print(f"Trip exported to {filename}")