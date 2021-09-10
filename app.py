import streamlit as st
import pandas as pd
import numpy as np

import requests

import pickle

df=pickle.load(open('movie_list.pkl','rb'))
similarity_score=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommendation System")
st.write("---- Made by Gourav Didwania ----")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_user):
    movie_index = df[df.title == movie_user].index.values[0]

    similar_movies = pd.DataFrame(enumerate(similarity_score[movie_index])).drop(0, axis='columns').sort_values(by=1, ascending=False)
    similar_movies['Names'] = list(map(lambda x: str(np.squeeze(df[df.index == x]['title'].values)), similar_movies.index.values))
    similar_movies['id'] = list(map(lambda x: int(np.squeeze(df[df.index == x]['id'].values)), similar_movies.index.values))

    recommended_movie_posters = []
    for i in range(13):
        id=similar_movies.id.values[i]
        # Fetch movie poster from the TMDB Database
        recommended_movie_posters.append(fetch_poster(id))

    return similar_movies.Names.values[:13],recommended_movie_posters


selected_movie = st.selectbox(
'Type or select a movie from the dropdown',
(list(df.title.values)))

if st.button('Show Recommendation'):
    names,poster = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    for i in range(1,len(names)):
        if ( i % 4 == 1):
            with col1:
                st.text(names[i])
                st.image(poster[i])
        elif (i % 4 == 2):
            with col2:
                st.text(names[i])
                st.image(poster[i])
        elif (i % 4 == 3):
            with col3:
                st.text(names[i])
                st.image(poster[i])
        elif (i % 4 == 0):
            with col4:
                st.text(names[i])
                st.image(poster[i])
