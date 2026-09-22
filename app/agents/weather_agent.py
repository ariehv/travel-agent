class WeatherAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Give typical weather information
        for travelers visiting {destination}.

        Include:

        - temperature
        - rainfall
        - clothing advice
        - seasonal considerations
        """