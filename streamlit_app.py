import streamlit as st
from data_processing import load_datasets
from content_based import ContentBasedRecommender
from collaborative import CollaborativeRecommender
from hybrid import HybridRecommender
from assistant import MovieAssistant

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie Recommendation Assistant",
    layout="wide"
)

st.title("🎬 Hybrid Movie Recommendation Assistant")
st.write("Personalized recommendations using Content + Collaborative Filtering")

# -----------------------------
# Load Data (Cached)
# -----------------------------
@st.cache_resource
def load_models():
    ratings, movies, credits, keywords, links = load_datasets()

    content_model = ContentBasedRecommender(movies)
    content_model.build_model()

    collab_model = CollaborativeRecommender(ratings)
    collab_model.build_model()

    hybrid_model = HybridRecommender(content_model, collab_model, movies, links)

    assistant = MovieAssistant(hybrid_model, movies)

    return assistant, movies

assistant, movies = load_models()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("User Settings")

user_id = st.sidebar.number_input("Enter User ID", min_value=1, value=1)

mode = st.sidebar.radio(
    "Recommendation Mode",
    ["By Movie Title", "By Genre"]
)

# -----------------------------
# Main UI
# -----------------------------

if mode == "By Movie Title":
    movie_list = movies['title'].dropna().unique()
    selected_movie = st.selectbox("Select a movie you like:", movie_list)

    if st.button("Get Recommendations"):
        response = assistant.handle_request(user_id, selected_movie)
        st.subheader("Recommended Movies:")
        st.write(response)

elif mode == "By Genre":
    genres = ["Action", "Comedy", "Drama", "Romance",
              "Thriller", "Horror", "Animation",
              "Adventure", "Fantasy", "Sci-Fi"]

    selected_genre = st.selectbox("Select Genre:", genres)

    if st.button("Show Movies"):
        response = assistant.handle_request(user_id, selected_genre)
        st.subheader("Top Movies:")
        st.write(response)
