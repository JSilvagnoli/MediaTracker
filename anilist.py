import requests
from datetime import date

anilist_url = "https://graphql.anilist.co"

def get_information(media_to_find: str, type: str):
    query = f"""
        query ($search: String!) {{
        Page {{
            media(search: $search, type: {type.upper()}) {{
                id
                title {{
                    english
                }}
                description
                startDate {{
                    day
                    month
                    year
                }}
                averageScore
            }}
        }}
    }}
    """

    variables = {
        'search': media_to_find
    }

    response = requests.post(
        anilist_url, 
        json={'query': query, 'variables': variables}
    )

    response.raise_for_status()
    return normalize_response(response.json(), type)

def normalize_response(response, type):
    normalized_data = []
    for result in response["data"]["Page"]["media"]:
        title = result.get("title")["english"]
        release_date_dict = result.get("startDate")
        if (
            release_date_dict is not None and 
            release_date_dict['year'] is not None and 
            release_date_dict['month'] is not None and
            release_date_dict['day'] is not None
        ):
            release_date = date(
                release_date_dict['year'],
                release_date_dict['month'],
                release_date_dict['day']
            )
            release_date = release_date.strftime("%Y-%m-%d")
        else:
            release_date = ""

        data_dict = {
            "id": result.get("id"),
            "title": title or "No Title Available",
            "description": result.get("description") or "No Descripton Available",
            "release_date": release_date or "No Release Date Available",
            "rating": result.get("averageScore") or "No Rating Available",
            "type": type
        }
        normalized_data.append(data_dict)

    return normalized_data

        