class HybridRecommender:
    def __init__(self, content_model, collab_model, movies, links):
        self.content_model = content_model
        self.collab_model = collab_model
        self.movies = movies
        self.links = links

    def recommend(self, user_id, title, top_n=10):
        content_recs = self.content_model.recommend(title, top_n=20)

        hybrid_scores = []

        for movie in content_recs:
            movie_row = self.movies[self.movies['title'] == movie]
            if movie_row.empty:
                continue

            tmdb_id = movie_row['id'].values[0]
            link_row = self.links[self.links['tmdbId'] == tmdb_id]

            if link_row.empty:
                continue

            movie_id = link_row['movieId'].values[0]
            collab_score = self.collab_model.predict(user_id, movie_id)

            hybrid_scores.append((movie, collab_score))

        hybrid_scores = sorted(hybrid_scores, key=lambda x: x[1], reverse=True)

        return [movie[0] for movie in hybrid_scores[:top_n]]
