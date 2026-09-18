class HiddenGemsAgent:

    def build_prompt(
        self,
        destination
    ):

        return f"""
        Give 10 hidden gems in
        {destination}.

        Include:

        - Local neighborhoods
        - Viewpoints
        - Cafes
        - Restaurants
        - Experiences

        Explain why each is special.
        """