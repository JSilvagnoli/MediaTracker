import requests

import storage

def main():
    url = 'https://api.themoviedb.org/3/search/movie'

    token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNzNiMDFhZDAwYWRkOGIyOTA1NzU0YjE3NmZlMTE0YyIsIm5iZiI6MTc4NjEyNDE3Ni4xODMsInN1YiI6IjZhNzYxNzkwMDI2NzU2M2EzYmUxMTBiZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Vm4_hC9Pb3JJeV1395DdwsQd9qRwltpH3Yh9Ri5ylhs"
    
    media_to_find = input("Please enter the name of the media you want to search for: ")

    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }

    params = {
        "query": media_to_find
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()

        data_to_display = []
        for result in data["results"]:
            #print(result.get("title") or result.get("name"))
            data_to_display.append(result.get("title") or result.get("name"))

        storage.save_json(data_to_display)

    else:
        print(f"Failed. Status code: {response.status_code}")

if __name__ == "__main__":
    main()