class RecommendationAgent:

    def recommend(
        self,
        budget,
        walking_level,
        previous_destinations
    ):

        candidates = [
            "Budapest",
            "Prague",
            "Krakow",
            "Vilnius",
            "Riga",
            "Tallinn",
            "Vienna",
            "Lisbon"
        ]

        recommendations = []

        for city in candidates:

            if city not in previous_destinations:

                recommendations.append(city)

        return recommendations[:3]