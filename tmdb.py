import requests
import os
from dotenv import load_dotenv

load_dotenv()

tmdb_movie_url = "https://api.themoviedb.org/3/search/movie"
tmdb_show_url = "https://api.themoviedb.org/3/search/tv"

tmdb_access_token = os.getenv("TMDB_ACCESS_TOKEN")

headers = {
    "Authorization": f"Bearer {tmdb_access_token}",
    "accept": "application/json"
}

def get_movie_information(movie_to_find):
    params = {
        "query": movie_to_find
    }

    response = requests.get(
        tmdb_movie_url, 
        headers=headers, 
        params=params
    )

    response.raise_for_status()
    return response.json()
        
def get_tv_information(show_to_find):
    params = {
        "query": show_to_find
    }
    
    response = requests.get(tmdb_show_url, headers=headers, params=params)
    
    response.raise_for_status()
    return response.json()