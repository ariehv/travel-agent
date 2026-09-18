class PackingAgent:

    def build_prompt(
        self,
        destination,
        days
    ):

        return f"""
        Create a packing list for a
        {days}-day trip to {destination}.

        Separate:

        - Essentials
        - Clothing
        - Electronics
        - Toiletries
        - Documents
        - Optional items

        Include luggage-saving tips.
        """