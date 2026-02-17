import pandas as pd

def load_datasets():
    ratings = pd.read_excel("data/ratings_small.xlsx")
    movies = pd.read_excel("data/movies_metadata.xlsx")
    credits = pd.read_excel("data/credits.xlsx")
    keywords = pd.read_excel("data/keywords.xlsx")
    links = pd.read_excel("data/links_small.xlsx")

    # Clean movie IDs
    movies = movies[['id', 'title', 'overview', 'genres']]
    movies = movies.dropna()
    movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
    movies = movies.dropna(subset=['id'])
    movies['id'] = movies['id'].astype(int)

    return ratings, movies, credits, keywords, links
