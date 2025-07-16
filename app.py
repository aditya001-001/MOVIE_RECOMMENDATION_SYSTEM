'''import pickle
import pandas as pd
import streamlit as st
import requests

st.title('Movie Recommendar System')




def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/7/movie/{}?api_key=c9ffd32736e63309d0f00762ad4de102&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances= similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


similarity= pickle.load(open('similarity.pkl','rb'))
movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

movie_selected = st.selectbox(
    "hey Baby",
    movies['title'].values
)

if st.button('Recommend'):
    names,posters= recommend(movie_selected)
    col1, col2, col3 , col4 ,col5= st.columns(5)


    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])'''


import streamlit as st
import pickle
import pandas as pd
import requests

# Fetch poster from TMDb API
def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=c9ffd32736e63309d0f00762ad4de102&language=en-US'
        response = requests.get(url, timeout=5)  # Add timeout to prevent hanging
        response.raise_for_status()

        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException as e:
        print(f"[Poster Fetch Error] Movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# Recommend top 5 similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        try:
            poster_url = fetch_poster(movie_id)
        except Exception as e:
            print(f"Error fetching poster for {title}: {e}")
            poster_url = "https://via.placeholder.com/500x750?text=Error"

        recommended_movies.append(title)
        recommended_posters.append(poster_url)

    return recommended_movies, recommended_posters

# Load data
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit UI
st.title("🎬 Movie Recommender System")

movie_selected = st.selectbox("Select a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(movie_selected)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

