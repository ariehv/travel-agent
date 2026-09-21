class FlightAgent:

    def build_prompt(
        self,
        origin,
        destination
    ):

        return f"""
        Suggest realistic flight routes from {origin} to {destination}.

        Include:

        - Direct flights if available           
        - Common connection airports
        - Typical flight duration
        - Recommended airlines
        - Airport codes
        """