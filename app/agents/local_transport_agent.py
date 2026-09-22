class LocalTransportAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Explain local transportation in
        {destination}.

        Include:

        - metro
        - buses
        - taxis
        - ride sharing
        - tourist transport passes
        """