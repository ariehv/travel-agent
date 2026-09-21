# show_trip_full.py

from app.repositories.trip_repository import get_trip

trip_id = int(input("Trip ID: "))

trip = get_trip(trip_id)

if not trip:
    print("Trip not found")
    exit()

print("\n" + "=" * 60)
print("TRIP INFORMATION")
print("=" * 60)

print(f"ID: {trip.id}")
print(f"Origin: {trip.origin}")
print(f"Destination: {trip.destination}")
print(f"Days: {trip.days}")

print("\n" + "=" * 60)
print("ITINERARY")
print("=" * 60)
print(trip.itinerary)

print("\n" + "=" * 60)
print("FOOD GUIDE")
print("=" * 60)
print(trip.food_guide)

print("\n" + "=" * 60)
print("PACKING LIST")
print("=" * 60)
print(trip.packing_list)

print("\n" + "=" * 60)
print("HIDDEN GEMS")
print("=" * 60)
print(trip.hidden_gems)

print("\n" + "=" * 60)
print("EMERGENCY PLAN")
print("=" * 60)
print(trip.emergency_plan)

print("\n" + "=" * 60)
print("OPTIMIZED ITINERARY")
print("=" * 60)
print(trip.optimized_itinerary)