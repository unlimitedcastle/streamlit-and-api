import requests

def get_movie_list_byGenre(genre_id, page=1):
    url = f'https://moviesapi.ir/api/v1/genres/{genre_id}/movies'
    api_parameters = {'page': page}
    response = requests.get(url, params=api_parameters)
    if response.status_code != 200:
        return 'ERROR'
    else:
        output = []
        response = response.json()
        response = response['data']
        for item in response:
            title = item['title']
            poster = item['poster']
            year = item['year']
            imdb_rate = item['imdb_rating']
            genres = item['genres']
            output.append([title, poster, year, imdb_rate, genres])
        return output


def get_genres_list():
    url = 'https://moviesapi.ir/api/v1/genres'
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        return response.json()