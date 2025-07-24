import pandas as pd
import pickle
import streamlit as st
import requests

# ✅ Correct fetch_poster using OMDb API
def fetch_poster(title):
    api_key = "56e6ff5d"  # Your actual activated OMDb API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    data = response.json()
    if data.get("Poster") and data["Poster"] != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Poster"

# ✅ Recommendation logic
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))

    return recommended_movie_names, recommended_movie_posters

# ✅ Load data
movies_data = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_data)

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_data = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_data)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox("Enter movie name:", movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    if recommended_movie_names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    else:
        
        st.warning("Movie not found in dataset!")














import os
import pickle

def download_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={"id": file_id}, stream=True)

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value
        return None

    token = get_confirm_token(response)

    if token:
        params = {"id": file_id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Download if not exists
if not os.path.exists("similarity.pkl"):
    download_from_google_drive("1tZEnt_kZNAZA3Mnet6h3q5LpE4-cDlSv", "similarity.pkl")

# Load the file
similarity = pickle.load(open("similarity.pkl", "rb"))

