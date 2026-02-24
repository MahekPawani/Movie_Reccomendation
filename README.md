#  IMDB Movie Recommendation System

A Streamlit-based movie recommendation system built with Python, NLP, TF-IDF similarity, fuzzy search, typo-tolerance, and a Family-Safe mode.  
Designed for academic submission, cross-platform compatibility, and clean reproducibility on any device.

## 📘 About This Project

This system recommends movies using **Content-Based Filtering**, powered by TF-IDF vectorization and cosine similarity.  
It includes smart search, typo tolerance, auto-suggestions, rating-based ranking, and multiple safety layers to filter adult/horror content.

### Key Features
-  **Case-Insensitive Search**
-  **Typo-Tolerant Search using Fuzzy Matching**
-  **“Did You Mean?” Auto-Suggestions**
-  **Content-Based Recommendations**
-  **Rating-Based Top 10 Movies**
-  **Family-Safe Mode** (removes unsafe keywords, adult titles, horror movies)
-  **Streamlit UI**
-  **Works on Mac, Windows, Linux, Google Colab, Jenkins, IDLE**
-  **Lightweight & Portable**

## 📂 Project Structure
<pre>
MovieRecommendation/
│
├── app.py
├── assistant.py
├── content_based.py
├── data_processing.py
├── moderation.py
├── streamlit_app.py
├── imdb_movies.csv
├── requirements.txt
├── README.md
└── .gitignore
</pre>


# How to Run the Project (All Environments)

This project supports 4 different execution environments:

- **Local Machine (VS Code / Terminal)**
- **Python IDLE**
- **Google Colab**
- **Jenkins CI Pipeline**

Each section below provides exact steps.

# 1. Run Locally (Mac / Windows / Linux)

### **Step 1 — Clone the Repository**
```bash
git clone https://github.com/MahekPawani/MovieRecommendation.git
cd MovieRecommendation

Step 2 — Create Virtual Environment

Mac / Linux

python3 -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

Step 3 — Install Requirements

pip install -r requirements.txt

Step 4 — Run the App

streamlit run app.py

Your browser will open at:
👉 http://localhost:8501/

⸻

2. Run in Python IDLE (Built-in Python Editor)

IDLE cannot display Streamlit UI, but it can run the backend.

Step 1 — Install Requirements (using Terminal)

pip install -r requirements.txt

Step 2 — Open Files in IDLE
	•	Open IDLE
	•	File → Open → select app.py

Step 3 — Run Using F5

IDLE will start the server.

Open the generated URL manually in your browser:

http://localhost:8501

⚠ Notes
	•	IDLE is for editing, not UI rendering
	•	Streamlit always opens in the browser

⸻

3️. Run on Google Colab (Cloud Environment)

Colab cannot natively host Streamlit UI → we use ngrok.

Step 1 — Clone Repo

!git clone https://github.com/MahekPawani/MovieRecommendation.git
%cd MovieRecommendation

Step 2 — Install Dependencies

!pip install -r requirements.txt
!pip install streamlit pyngrok

Step 3 — Create Public Tunnel

from pyngrok import ngrok
public_url = ngrok.connect(8501)
public_url

Step 4 — Run Streamlit

!streamlit run app.py --server.port 8501 --server.headless true

Click the public URL → Streamlit runs online.

⚠ Notes
	•	Streamlit runs in a separate process
	•	Close the ngrok tunnel when done

⸻

4️. Run on Jenkins (CI/CD Pipeline)

Jenkins is used for automated builds, not UI rendering.

Step 1 — Add This Pipeline Script

pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/MahekPawani/MovieRecommendation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Code Validation') {
            steps {
                sh '. venv/bin/activate && python3 -m py_compile *.py'
            }
        }

        stage('Run Streamlit (Optional)') {
            steps {
                sh '. venv/bin/activate && nohup streamlit run app.py --server.port 8501 &'
            }
        }
    }
}

 Notes
	•	Jenkins cannot display Streamlit UI
	•	The app runs on server IP: http://<server-ip>:8501
	•	Use this mostly for testing, building, verifying code

⸻

👥 Authors
	•	Mahek Pawani
	•	Swara Kuthe
	•	Rishit Nakra
	•	Dhruv Motwani

⸻

 Final Notes
	•	This project is compatible with Mac, Windows, Linux
	•	Runs on local machines, cloud notebooks, and CI pipelines
	•	Clean .gitignore ensures reproducible builds
	•	Fuzzy search + family-safe filtering make it user-friendly
