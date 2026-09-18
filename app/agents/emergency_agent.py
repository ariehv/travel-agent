class EmergencyAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Create a travel backup plan
        for {destination}.

        Cover:

        - Flight delays
        - Lost luggage
        - Weather problems
        - Missed transportation
        - Illness
        - Lost passport

        Give practical actions.
        """