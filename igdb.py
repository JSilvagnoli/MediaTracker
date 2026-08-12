from requests import post
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

igdb_client_id = os.getenv("IGDB_TWITCH_CLIENT_ID")
igdb_client_secret = os.getenv("IGDB_TWITCH_CLIENT_SECRET")

# Get Twitch access token
def get_igdb_access_token():
    access_token_url = "https://id.twitch.tv/oauth2/token"

    token_params = {
        "client_id": igdb_client_id,
        "client_secret": igdb_client_secret,
        "grant_type": "client_credentials"
    }

    token_response = post(
        access_token_url,
        params=token_params
    )

    token_response.raise_for_status()

    igdb_access_token = token_response.json()["access_token"]
    return igdb_access_token

def get_information(game_to_find):
    igdb_access_token = get_igdb_access_token()

    igdb_url = "https://api.igdb.com/v4/games"
        
    headers = {
        "Client-ID": igdb_client_id,
        "Authorization": f"Bearer {igdb_access_token}"
    }

    query = f"""
    search "{game_to_find}";
    fields id, name, summary, first_release_date, rating;
    """

    response = post(
        igdb_url,
        headers=headers,
        data=query
    )

    response.raise_for_status()

    return normalize_response(response.json())

def normalize_response(response):
    normalized_data = []
    for result in response:
        data_dict = {
            "id": result.get("id"),
            "title": result.get("name") or "No Title Available",
            "description": result.get("summary") or "No Description Available",
            "release_date": convert_release_date(result.get("first_release_date")),
            "rating": result.get("rating") or "No Rating Available",
            "type": "game"
        }
        normalized_data.append(data_dict)

    return normalized_data

def convert_release_date(unix_time_stamp):
    if unix_time_stamp is None:
        return "No Release Date Available"
    else:
        return datetime.fromtimestamp(unix_time_stamp).strftime("%Y-%m-%d")