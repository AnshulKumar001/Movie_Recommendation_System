import pandas as pd
import pickle
import streamlit as st
import requests
import os

# ✅ Fetch poster using OMDb API
def fetch_poster(title):
    api_key = "56e6ff5d"  # Replace with your OMDb API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    data = response.json()
    return data.get("Poster") if data.get("Poster") and data["Poster"] != "N/A" else "https://via.placeholder.com/300x450?text=No+Poster"

# ✅ Download from Google Drive
def download_from_google_drive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={"id": file_id}, stream=True)

    token = None
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            token = value
            break

    if token:
        response = session.get(URL, params={"id": file_id, "confirm": token}, stream=True)

    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# ✅ Ensure required files exist
if not os.path.exists("movies.pkl"):
    download_from_google_drive("1tZEnt_kZNAZA3Mnet6h3q5LpE4-cDlSv", "movies.pkl")

if not os.path.exists("similarity.pkl"):
    download_from_google_drive("1tZEnt_kZNAZA3Mnet6h3q5LpE4-cDlSv", "similarity.pkl")

# ✅ Load data once
movies = pd.DataFrame(pickle.load(open("movies.pkl", "rb")))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ✅ Recommendation logic
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances:
        title = movies.iloc[i[0]].title
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))

    return recommended_movie_names, recommended_movie_posters

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

