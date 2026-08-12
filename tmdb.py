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

def get_information(media_to_find, media_type):
    params = {
        "query": media_to_find
    }

    url = tmdb_movie_url if media_type == "movie" else tmdb_show_url

    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    return normalize_response(response.json(), media_type)

def normalize_response(response, media_type):
    normalized_data = []
    for result in response["results"]:
        title = result.get("title") if media_type == "movie" else result.get("name")
        release_date = (
            result.get("release_date")
            if media_type == "movie"
            else result.get("first_air_date")
        )
        data_dict = {
            "id": result.get("id"),
            "title": title or "No Title Available",
            "description": result.get("overview") or "No Descripton Available",
            "release_date": release_date or "No Release Date Available",
            "rating": result.get("vote_average") or "No Rating Available",
            "type": media_type
        }
        normalized_data.append(data_dict)

    return normalized_data