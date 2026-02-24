# content_based.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentRecommender:

    def __init__(self, df):
        self.df = df.reset_index(drop=True)
        self.tfidf = None
        self.similarity_matrix = None

    def build_model(self):
        """
        Builds TF-IDF model using description + genre.
        """

        # Combine useful text features
        self.df["combined_features"] = (
            self.df["description"].fillna("") + " " +
            self.df["genre"].fillna("")
        )

        # Create TF-IDF matrix
        self.tfidf = TfidfVectorizer(stop_words="english")

        tfidf_matrix = self.tfidf.fit_transform(
            self.df["combined_features"]
        )

        # Compute cosine similarity
        self.similarity_matrix = cosine_similarity(tfidf_matrix)

    def recommend(self, movie_title, top_n=10):
        """
        Returns list of recommended movie titles.
        """

        if not movie_title:
            return []

        movie_title = movie_title.lower().strip()

        # Check if movie exists
        matches = self.df[
            self.df["title"].str.lower() == movie_title
        ]

        if matches.empty:
            return []

        idx = matches.index[0]

        # Get similarity scores
        sim_scores = list(
            enumerate(self.similarity_matrix[idx])
        )

        # Sort movies by similarity score
        sim_scores = sorted(
            sim_scores,
            key=lambda x: x[1],
            reverse=True
        )

        # Remove itself
        sim_scores = sim_scores[1: top_n + 1]

        recommendations = []

        for i, _ in sim_scores:
            if 0 <= i < len(self.df):
                recommendations.append(
                    self.df.iloc[i]["title"]
                )

        return recommendations