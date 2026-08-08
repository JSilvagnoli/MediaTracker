import requests

tmdb_url = 'https://api.themoviedb.org/3/search/movie'

tmdb_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNzNiMDFhZDAwYWRkOGIyOTA1NzU0YjE3NmZlMTE0YyIsIm5iZiI6MTc4NjEyNDE3Ni4xODMsInN1YiI6IjZhNzYxNzkwMDI2NzU2M2EzYmUxMTBiZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Vm4_hC9Pb3JJeV1395DdwsQd9qRwltpH3Yh9Ri5ylhs"

headers = {
    "Authorization": f"Bearer {tmdb_token}",
    "accept": "application/json"
}

def get_movie_information(movie_to_find):
    params = {
        "query": movie_to_find
    }

    response = requests.get(tmdb_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed. Status code: {response.status_code}")