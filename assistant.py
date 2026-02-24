class MovieAssistant:
    def __init__(self, recommender, df):
        self.recommender = recommender
        self.df = df

    def handle_request(self, user_input):

        if not user_input or not user_input.strip():
            return []

        recommendations = self.recommender.recommend(user_input)

        if not recommendations:
            return []

        return recommendations