class FoodAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Create a complete food guide
        for {destination}.

        Include:

        - Best local dishes
        - Affordable restaurants
        - Premium restaurants
        - Food markets
        - Street food
        - Typical meal prices

        Format clearly.
        """