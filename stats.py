from collections import Counter

from app.repositories.trip_repository import list_trips


def main():

    trips = list_trips()

    if not trips:
        print()
        print("No trips found.")
        return

    # Get destinations
    destinations = [
        trip.destination
        for trip in trips
        if trip.destination
    ]

    # Get trip lengths
    lengths = [
        trip.days
        for trip in trips
        if trip.days is not None
    ]

    print()
    print("Travel Agent Statistics")
    print("=" * 40)
    print()

    # Total trips
    print(f"Total trips: {len(trips)}")

    # Most frequent destination
    if destinations:

        destination_counter = Counter(destinations)

        destination, count = (
            destination_counter.most_common(1)[0]
        )

        print(
            f"Most planned destination: "
            f"{destination} ({count} trips)"
        )

    else:
        print("Most planned destination: N/A")

    # Average trip length
    if lengths:

        average_days = sum(lengths) / len(lengths)

        print(
            f"Average trip length: "
            f"{average_days:.1f} days"
        )

        print(
            f"Longest trip: "
            f"{max(lengths)} days"
        )

        print(
            f"Shortest trip: "
            f"{min(lengths)} days"
        )

    else:

        print("Average trip length: N/A")
        print("Longest trip: N/A")
        print("Shortest trip: N/A")

    print()
    print("=" * 40)


if __name__ == "__main__":
    main()