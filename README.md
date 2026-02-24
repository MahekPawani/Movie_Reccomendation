
# Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit.

This project provides intelligent movie recommendations based on movie content similarity using TF-IDF vectorization and cosine similarity.

---

## Features

- Content-Based Recommendation System
- TF-IDF + Cosine Similarity
- Case-Insensitive Search
- Typo Tolerance (Fuzzy Matching)
- Family Safe Mode (Content Filtering)
- Horror Genre Filtering (in Family Mode)
- Clean Streamlit Web Interface
- "Show More" Dynamic Result Display
- Safe Homepage Recommendations

---

## How It Works

1. Movie metadata is processed using TF-IDF vectorization.
2. Cosine similarity is used to compute similarity between movies.
3. When a user searches for a movie:
   - Exact case-insensitive match is attempted.
   - If not found, fuzzy string matching suggests closest title.
4. Recommendations are generated based on similarity scores.
5. Family Safe Mode filters adult content and horror genre.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Project Structure
MovieRecommendation/
│
├── app.py
├── assistant.py
├── content_based.py
├── data_processing.py
├── moderation.py
├── imdb_movies.csv
├── requirements.txt
├── README.md
└── .gitignore

---

##  How to Run Locally

### 1.Clone the repository
git clone <your-repository-url>
cd MovieRecommendation

### 2.Install dependencies
pip install -r requirements.txt

### 3. Run the application
streamlit run app.py

The application will open in your browser automatically.

---

##  Family Safe Mode

When enabled:
- Filters movies containing unsafe keywords
- Removes horror genre movies
- Applies filtering to both search results and homepage recommendations

---

##  Academic Context

This project was developed as part of coursework in **Open Source Tools for Data Science / Data Science**.

It demonstrates:
- Data preprocessing using Pandas
- Text vectorization using TF-IDF
- Similarity-based recommendation systems
- Fuzzy string matching
- Interactive web app deployment using Streamlit

---

##  Future Improvements (Optional)

- Display movie ratings in search results
- Add certification labels (U / U/A / A)
- Implement hybrid recommendation system
- Add user personalization

---

##  Author
- Mahek Pawani
- Swara Kuthe
- Rishit Nakra
- Dhruv Motwani

---
## Reviewer
   Vikas Choudhary
## 📌 Notes

- This project uses relative file paths for portability.
- The system runs locally, on Jenkins, and in cloud notebook environments with minimal configuration.
- No deep learning or external APIs are used.

---
