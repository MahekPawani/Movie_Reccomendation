class MovieAssistant:
    def __init__(self, hybrid_model, movies):
        self.hybrid_model = hybrid_model
        self.movies = movies

    # -----------------------------
    # Title Extraction (Safe)
    # -----------------------------
    def extract_title(self, text):
        if not isinstance(text, str):
            return None

        text = text.lower()

        for title in self.movies['title']:
            if not isinstance(title, str):
                continue

            if title.lower() in text:
                return title

        return None

    # -----------------------------
    # Genre Extraction (Safe)
    # -----------------------------
    def extract_genre(self, text):
        if not isinstance(text, str):
            return None

        genres = [
            "Action", "Comedy", "Drama", "Romance",
            "Thriller", "Horror", "Animation",
            "Adventure", "Fantasy", "Sci-Fi"
        ]

        text = text.lower()

        for genre in genres:
            if genre.lower() in text:
                return genre

        return None

    # -----------------------------
    # Handle Title Request
    # -----------------------------
    def _handle_title(self, user_id, title):
        recommendations = self.hybrid_model.recommend(
            user_id=user_id,
            title=title,
            top_n=5
        )

        if not recommendations:
            return "Sorry, I couldn’t find similar movies."

        response = f"Because you liked '{title}', you might enjoy:\n"
        for movie in recommendations:
            response += f"- {movie}\n"

        return response

    # -----------------------------
    # Handle Genre Request
    # -----------------------------
    def _handle_genre(self, genre):

        if 'genres' not in self.movies.columns:
            return "Genre information not available in dataset."

        filtered = self.movies[
            self.movies['genres'].astype(str).str.contains(
                genre, case=False, na=False
            )
        ]

        top_movies = filtered['title'].head(5).tolist()

        if not top_movies:
            return f"I couldn't find {genre} movies."

        response = f"Here are some {genre} movies:\n"
        for movie in top_movies:
            response += f"- {movie}\n"

        return response

    # -----------------------------
    # Main Entry Function
    # -----------------------------
    def handle_request(self, user_id, user_input, mode="auto"):
        """
        mode:
        - "title" → Direct movie title mode
        - "genre" → Direct genre mode
        - "auto"  → NLP detection mode
        """

        # Direct Title Mode (from dropdown)
        if mode == "title":
            return self._handle_title(user_id, user_input)

        # Direct Genre Mode (from dropdown)
        if mode == "genre":
            return self._handle_genre(user_input)

        # Auto NLP Mode (free text input)
        title = self.extract_title(user_input)
        genre = self.extract_genre(user_input)

        if title:
            return self._handle_title(user_id, title)

        elif genre:
            return self._handle_genre(genre)

        else:
            return "Please mention a movie title or genre so I can help you."
