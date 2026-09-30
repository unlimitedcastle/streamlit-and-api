import streamlit as st
import app_api

st.title('Genres List')
genres_data = app_api.get_genres_list()

if genres_data == 'ERROR':
    st.error('Error')
else:
    genre_names = []
    for item in genres_data:
        genre_names.append(item['name'])
    
    select_genre = st.selectbox('select genres: ', genre_names)
    
    select_genreid = None
    for item in genres_data:
        if item['name'] == select_genre:
            select_genreid = item['id']
    
    movie_page = st.number_input('enter a nember page', min_value=1)
    
    if st.button('checking'):
        result = app_api.get_movie_list_byGenre(select_genreid, movie_page)
        if result != 'ERROR':
            st.write(result)
        else:
            st.error('INFO NOT FOUND')