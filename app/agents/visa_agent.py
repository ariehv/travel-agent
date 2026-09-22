class VisaAgent:

    def build_prompt(
        self,
        origin,
        destination
    ):

        return f"""
        Explain visa considerations for
        travelers from {origin}
        visiting {destination}.

        Include:

        - visa requirements
        - passport validity
        - entry considerations

        Mention that official sources
        should always be checked.
        """