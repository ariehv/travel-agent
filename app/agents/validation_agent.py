class ValidationAgent:

    def build_prompt(
        self,
        destination,
        itinerary
    ):

        return f"""
        Review this itinerary for {destination}.

        Check:

        - geographic accuracy
        - transportation accuracy
        - attraction existence
        - hotel area validity
        - airport information

        Remove mistakes.

        Return corrected itinerary.

        {itinerary}
        """