import streamlit as st
import pickle
import  pandas as pd
import requests

def fetch_poster(movies_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9c23b80316314e6243950a1725317282'.format(movies_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    recommended_movies_poster=[]
    movie_index=movies[movies['title']==movie].index[0]

    distance = similarity[movie_index]
    movies_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])
    recommended_movies=[]
    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('movies Recommender system ')

selected_movie_name = st.selectbox('search Movie for recommended',movies['title'].values)

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(poster[i])





