class FlightAgent:

    def search(self, origin, destination):

        return {
            "origin": origin,
            "destination": destination,
            "route": f"{origin} → Madrid → {destination}"
        }