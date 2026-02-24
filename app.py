import streamlit as st
from data_processing import load_dataset
from content_based import ContentRecommender
from assistant import MovieAssistant
from moderation import contains_unsafe_words
import difflib


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="IMDB Movie Recommender",
    layout="wide"
)

st.title("Movie Recommendation System")


# -------------------------------------------------
# LOAD SYSTEM
# -------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_system():

    df = load_dataset()
    df.fillna("", inplace=True)

    recommender = ContentRecommender(df)
    recommender.build_model()

    assistant = MovieAssistant(recommender, df)

    return assistant, df


assistant, df = load_system()


# -------------------------------------------------
# SESSION STATE INIT
# -------------------------------------------------
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "show_all" not in st.session_state:
    st.session_state.show_all = False


# -------------------------------------------------
# SIDEBAR SETTINGS
# -------------------------------------------------
st.sidebar.header("Settings")
force_family_mode = st.sidebar.checkbox("Force Family Safe Mode")


# -------------------------------------------------
# 🔍 SEARCH SECTION
# -------------------------------------------------
st.header("🔍 Search for a Movie")

user_input = st.text_input("Enter movie name")

if st.button("Get Recommendations"):

    st.session_state.show_all = False  # Reset show more on new search

    if not user_input.strip():
        st.warning("Please enter a movie name.")
        st.session_state.recommendations = []

    else:

        user_input_clean = user_input.strip().lower()

        # Ensure lowercase column exists
        if "title_lower" not in df.columns:
            df["title_lower"] = df["title"].str.lower()

        # Exact match
        movie_row = df[df["title_lower"] == user_input_clean]

        # Fuzzy match if not found
        if movie_row.empty:

            possible_matches = difflib.get_close_matches(
                user_input_clean,
                df["title_lower"].tolist(),
                n=1,
                cutoff=0.6  # More flexible
            )

            if possible_matches:
                suggestion = possible_matches[0]
                st.info(f"Did you mean: {suggestion.title()} ?")
                movie_row = df[df["title_lower"] == suggestion]
            else:
                st.error("Movie not found in dataset.")
                st.session_state.recommendations = []
                movie_row = None

        # If movie found
        if movie_row is not None and not movie_row.empty:

            # Family mode: block horror
            if force_family_mode and "horror" in str(movie_row.iloc[0]["genre"]).lower():
                st.warning("This movie is restricted in Family Safe Mode.")
                st.session_state.recommendations = []
            else:

                recommendations = assistant.handle_request(movie_row.iloc[0]["title"])

                if recommendations:

                    # Remove duplicates
                    seen = set()
                    clean_recommendations = []

                    for movie in recommendations:
                        if movie not in seen:
                            clean_recommendations.append(movie)
                            seen.add(movie)

                    # Apply family filtering to results
                    if force_family_mode:
                        filtered = []

                        for movie in clean_recommendations:
                            row = df[df["title"] == movie]

                            if not row.empty:
                                title = row.iloc[0]["title"]
                                description = row.iloc[0]["description"]
                                genre = str(row.iloc[0]["genre"]).lower()

                                if (
                                    not contains_unsafe_words(title)
                                    and not contains_unsafe_words(description)
                                    and "horror" not in genre
                                ):
                                    filtered.append(movie)

                        st.session_state.recommendations = filtered
                    else:
                        st.session_state.recommendations = clean_recommendations

                else:
                    st.session_state.recommendations = []


# -------------------------------------------------
# DISPLAY RECOMMENDATIONS
# -------------------------------------------------
recommendations = st.session_state.recommendations

if recommendations:

    st.subheader("Recommended Movies")

    if st.session_state.show_all:
        movies_to_display = recommendations
    else:
        movies_to_display = recommendations[:5]

    for movie in movies_to_display:
        st.markdown(
            f"<small>• {movie}</small>",
            unsafe_allow_html=True
        )

    if len(recommendations) > 5 and not st.session_state.show_all:
        if st.button("Show More"):
            st.session_state.show_all = True
            st.rerun()


# -------------------------------------------------
# TODAY'S RECOMMENDATIONS
# -------------------------------------------------
st.markdown("---")
st.header("Today's Recommendations")

safe_homepage = df[
    (~df["description"].apply(contains_unsafe_words)) &
    (~df["title"].apply(contains_unsafe_words))
]

if force_family_mode:
    safe_homepage = safe_homepage[
        ~safe_homepage["genre"].str.lower().str.contains("horror", na=False)
    ]

safe_homepage = safe_homepage.sort_values(
    by="rating",
    ascending=False
).head(10)

if not safe_homepage.empty:
    for _, movie in safe_homepage.iterrows():
        st.markdown(
            f"<small>• {movie['title']}</small>",
            unsafe_allow_html=True
        )
else:
    st.info("No safe recommendations available.")