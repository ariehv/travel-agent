class HotelAgent:

    def build_prompt(self, destination):

        return f"""
        Recommend hotel areas in {destination}.

        Include:

        - Area name
        - Budget level
        - Advantages
        - Walking friendliness
        """