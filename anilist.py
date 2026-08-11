import requests

anilist_url = "https://graphql.anilist.co"

def get_anime_information(anime_to_find):
    query = """
        query ($search: String!) {
        Page {
            media(search: $search, type: ANIME) {
                id
                title {
                    english
                }
                description
                startDate {
                    day
                    month
                    year
                }
                averageScore
            }
        }
    }
    """

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': anime_to_find
    }

    response = requests.post(
        anilist_url, 
        json={'query': query, 'variables': variables}
    )

    response.raise_for_status()
    return response.json()

def get_manga_information(manga_to_find):
    query = """
        query ($search: String!) {
        Page {
            media(search: $search, type: MANGA) {
                id
                title {
                    english
                }
                description
                startDate {
                    day
                    month
                    year
                }
                averageScore
            }
        }
    }
    """

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': manga_to_find
    }

    response = requests.post(
        anilist_url, 
        json={'query': query, 'variables': variables}
    )

    response.raise_for_status()
    return response.json()

                                            