from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

class CollaborativeRecommender:
    def __init__(self, ratings):
        self.ratings = ratings
        self.model = SVD()

    def build_model(self):
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(
            self.ratings[['userId', 'movieId', 'rating']], reader
        )
        trainset, _ = train_test_split(data, test_size=0.2)
        self.model.fit(trainset)

    def predict(self, user_id, movie_id):
        return self.model.predict(user_id, movie_id).est
