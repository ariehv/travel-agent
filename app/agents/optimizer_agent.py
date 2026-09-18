class OptimizerAgent:

    def build_prompt(
        self,
        destination,
        days
    ):

        return f"""
        Optimize a {days}-day trip
        to {destination}.

        Minimize travel time.

        Group nearby attractions.

        Suggest a better order
        of visits.

        Explain improvements.
        """