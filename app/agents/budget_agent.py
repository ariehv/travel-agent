class BudgetAgent:

    def estimate(self, budget_level):

        if budget_level == "budget":
            return "$50-$100 per day"

        if budget_level == "moderate":
            return "$100-$200 per day"

        if budget_level == "luxury":
            return "$250-$500 per day"

        return "Unknown"