import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedRecommender:
    def __init__(self, movies):
        self.movies = movies
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.similarity_matrix = None
        self.indices = None

    def build_model(self):
        self.movies['overview'] = self.movies['overview'].fillna('')
        tfidf_matrix = self.tfidf.fit_transform(self.movies['overview'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        self.indices = pd.Series(self.movies.index, index=self.movies['title']).drop_duplicates()

    def recommend(self, title, top_n=10):
        if title not in self.indices:
            return []

        idx = self.indices[title]

        # Force single index
        if isinstance(idx, pd.Series):
            idx = idx.iloc[0]

        sim_scores = list(enumerate(self.similarity_matrix[idx]))

        # Ensure similarity score is float
        sim_scores = [(i, float(score)) for i, score in sim_scores]

        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        sim_scores = sim_scores[1:top_n+1]

        movie_indices = [i[0] for i in sim_scores]

        return self.movies['title'].iloc[movie_indices].tolist()

