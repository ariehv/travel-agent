class CurrencyAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Explain local currency information
        for visitors to {destination}.

        Include:

        - currency name
        - payment methods
        - ATM availability
        - tipping customs
        """