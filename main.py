import requests

def main():
    url = 'https://api.themoviedb.org/3/'
    media_to_find = input("Please enter the name of the media you want to search for: ")
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    main()