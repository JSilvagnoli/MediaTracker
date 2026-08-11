import sqlite3

import ui
import tmdb
import database
import igdb
import anilist

def main():
    database.create_movie_database()
    database.create_show_database()
    database.create_game_database()
    database.create_anime_database()
    database.create_manga_database()

    while True:
        handle_menu_choice(ui.display_menu())

def handle_menu_choice(user_input):
    handler = MENU_CHOICES.get(user_input)
    if handler:
        handler()

def handle_get_movie():
    while True:
        movie_to_find = ui.get_media_title()
        found_movies = tmdb.get_movie_information(movie_to_find)
        selected_movies = ui.display_movie_information_found(found_movies)
        
        if selected_movies is not None:
            handle_add_movie_to_database(selected_movies)
            database.display_movie_database()
            
        if ui.search_for_more_media().lower() != "y":
            break

def handle_get_show():
    while True: 
        show_to_find = ui.get_media_title()
        found_shows = tmdb.get_tv_information(show_to_find)
        selected_shows = ui.display_show_information_found(found_shows)

        if selected_shows is not None:
            handle_add_show_to_database(selected_shows)
            database.display_show_database()

        if (ui.search_for_more_media() == "y"):
            continue
        else:
            break

def handle_get_game():
    access_token = igdb.get_igdb_access_token()

    while True:
        game_to_find = ui.get_media_title()
        found_games = igdb.get_game_information(access_token, game_to_find)
        selected_games = ui.display_game_information_found(found_games)

        if selected_games is not None:
            handle_add_game_to_database(selected_games)
            database.display_game_database()

        if (ui.search_for_more_media() == "y"):
            continue
        else:
            break

def handle_get_anime():
    while True:
        anime_to_find = ui.get_media_title()
        found_anime = anilist.get_anime_information(anime_to_find)
        selected_anime = ui.display_anime_information_found(found_anime)

        if selected_anime is not None:
            handle_add_anime_to_database(selected_anime)
            database.display_anime_database()

        if (ui.search_for_more_media() == "y"):
            continue
        else:
            break

def handle_get_manga():
    while True:
        manga_to_find = ui.get_media_title()
        found_manga = anilist.get_manga_information(manga_to_find)
        selected_manga = ui.display_manga_information_found(found_manga)

        if selected_manga is not None:
            handle_add_manga_to_database(selected_manga)
            database.display_manga_database()

        if (ui.search_for_more_media() == "y"):
            continue
        else:
            break


def handle_add_movie_to_database(response):
    database.add_movie_to_database(response)
    
def handle_add_show_to_database(response):
    database.add_show_to_database(response)

def handle_add_game_to_database(response):
    database.add_game_to_database(response)

def handle_add_anime_to_database(response):
    database.add_anime_to_database(response)

def handle_add_manga_to_database(response):
    database.add_manga_to_database(response)

MENU_CHOICES = {
    '1': handle_get_movie,
    '2': handle_get_show,
    '3': handle_get_game,
    '4': handle_get_anime,
    '5': handle_get_manga
}

if __name__ == "__main__":
    main()