# 🎬 Movie Recommendation System Using Machine Learning 

A Movie Recommendation System that suggests movies to users based on their preferences.  
The system uses machine learning techniques to analyze movie data and recommend similar movies.

---

## 🚀 Features

- Recommend movies based on similarity
- Search movies by title
- Content-based filtering
- Fast recommendations using cosine similarity
- Simple and interactive interface

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit** (for web app)
- **TMDB Dataset**

---

## 📂 Project Structure

```
Movie-Recommendation-System
│
├── app.py                # Streamlit web application
├── model.py              # Recommendation logic
├── movies.csv            # Movie dataset
├── similarity.pkl        # Precomputed similarity matrix
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---

## ⚙️ How It Works

1. Movie dataset is loaded.
2. Important features like **genres, keywords, cast, and overview** are combined.
3. Text data is converted into vectors using **CountVectorizer / TF-IDF**.
4. **Cosine similarity** is calculated between movies.
5. When a user selects a movie, the system returns the most similar movies.

---

## 📊 Algorithm Used

- Content-Based Filtering
- Cosine Similarity
- Natural Language Processing (NLP)

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
```

Move into the project folder:

```bash
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎥 Example Output

Input:
```
Avatar
```

Recommended Movies:
- Guardians of the Galaxy
- Star Trek
- John Carter
- The Avengers
- Interstellar

---

## 📈 Future Improvements

- Add collaborative filtering
- Use deep learning models
- Integrate with TMDB API for posters
- Deploy on cloud (AWS / Render / Hugging Face)

---

## 👨‍💻 Author

**Ansh**  
B.Tech Computer Science  
AI / ML Enthusiast

---
