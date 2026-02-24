import pandas as pd


def load_dataset():

    df = pd.read_csv("imdb_movies.csv")

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    # -----------------------------
    # Rename correctly for YOUR dataset
    # -----------------------------
    df = df.rename(columns={
        "names": "title",
        "overview": "description",
        "score": "rating"
    })

    # If orig_title exists but names is empty, fallback
    if "orig_title" in df.columns:
        df["title"] = df["title"].fillna(df["orig_title"])

    # Ensure required columns exist now
    required_cols = ["title", "description", "genre"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # -----------------------------
    # Clean core columns
    # -----------------------------
    df = df.dropna(subset=["title", "description"])

    df["title"] = df["title"].astype(str).str.strip()
    df["description"] = df["description"].astype(str)
    df["genre"] = df["genre"].fillna("").astype(str)

    # -----------------------------
    # Convert rating safely
    # -----------------------------
    if "rating" in df.columns:
        df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # -----------------------------
    # Family-friendly detection
    # -----------------------------
    family_keywords = [
        "animation",
        "family",
        "children",
        "kids",
        "fantasy",
        "adventure"
    ]

    def is_family(text):
        text = str(text).lower()
        return any(k in text for k in family_keywords)

    df["is_family_friendly"] = df["genre"].apply(is_family)

    # -----------------------------
    # Memory guard (safe)
    # -----------------------------
    MAX_MOVIES = 15000

    if len(df) > MAX_MOVIES:
        df = df.sample(MAX_MOVIES, random_state=42).reset_index(drop=True)

    df = df.reset_index(drop=True)
    return df 
    
