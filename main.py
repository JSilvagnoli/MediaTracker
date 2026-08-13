from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import ui
import database
import tmdb
import igdb
import anilist

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():    
    while True:
        type = ui.display_menu()
        database.create_database(type)
        handle_get_media(type)

def handle_get_media(media_type):
    while True:
        packaged_media = get_media(media_type)

        if not packaged_media:
            return None
        
        add_to_database(packaged_media, media_type)

        if not ui.confirm("Would you like to add something else?"):
            break

def get_media(media_type):
    media_to_find = ui.get_media_name()
    
    if not media_to_find:
        return None

    if media_type == "movie" or media_type == "show":
        found_media = tmdb.get_information(media_to_find, media_type)
    elif media_type == "game":
        found_media = igdb.get_information(media_to_find)
    elif media_type == "anime" or media_type == "manga":
        found_media = anilist.get_information(media_to_find, media_type)
    else:
        return None

    ui.display_information_found(found_media)

    selected_media = ui.select_media(found_media)

    if selected_media is None:
        return None

    if not ui.confirm("Would you like to save this media?"):
        return None

    return selected_media

def add_to_database(media, media_type):
    if media is not None:
        database.add_to_database(media)
        database.display_database(media_type)

@app.get("/")
def get_information(media_to_find: str):
    return {"search": media_to_find}

@app.get("/search")
def search_media(media_to_find: str, media_type: str):
    if media_type == "movie" or media_type == "show":
        return tmdb.get_information(media_to_find, media_type)
    elif media_type == "game":
        return igdb.get_information(media_to_find)
    elif media_type == "anime" or media_type == "manga":
        return anilist.get_information(media_to_find, media_type)

if __name__ == "__main__":
    main()