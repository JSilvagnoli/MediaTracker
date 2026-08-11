from datetime import datetime, date

def display_menu():
    print("=====================")
    print("    Media Tracker    ")
    print("=====================")

    print("---------------------")
    print("1. Search For Movie")
    print("2. Search For Show")
    print("3. Search For Game")
    print("4. Search For Anime")
    print("5. Search For Manga")
    print()

    while True:
        user_input = input("What would you like to do? (Enter 1, 2, 3, 4, ...): ")
        if user_input in ("1", "2", "3", "4", "5"):
            return user_input

def get_media_title():
    return input("Please enter the name of the media you want to search for: ")

def search_for_more_media():
    return input("Would you like to search for something else? (Y/N): ")

def display_movie_information_found(response):
    data_to_add = []
    i = 1
    for result in response['results']:
        print(
        f"ID: {i}\n"
        f"Name: {result.get('title')}\n"
        f"Release Date: {datetime.strptime(result.get('release_date'), '%Y-%m-%d').strftime('%B %d, %Y')}\n"
        f"Description: {result.get('overview')}\n"
        )
        i += 1
    while True:
        choice = input("Please enter the ID of the movie you want to add: ")
        if choice.isdigit() and 1 <= int(choice) <= len(response['results']):
            add_to_database = input("Would you like to save this movie? (Y/N): ")
            if (add_to_database.lower() == "y"):
                data_to_add.append(
                    [
                        response['results'][int(choice) - 1].get("id"),
                        response['results'][int(choice) - 1].get("title"),
                        response['results'][int(choice) - 1].get("overview"),
                        response['results'][int(choice) - 1].get("release_date"),
                        response['results'][int(choice) - 1].get("vote_average"),
                    ]
                )                
            elif (add_to_database.lower() == "n"):
                break
            else:
                print("Please type (Y/N)")
                continue
        else:
            continue
        
        add_another = input("Would you like to add another movie from the list? (Y/N): ")
        if (add_another.lower() == "y"):
            continue
        elif (add_another.lower() == "n"):
            return data_to_add
        else:
            return None
        
def display_show_information_found(response):
    data_to_add = []
    i = 1
    for result in response['results']:
        print(
        f"ID: {i}\n"
        f"Name: {result.get('name')}\n"
        f"Release Date: {datetime.strptime(result.get('first_air_date'), '%Y-%m-%d').strftime('%B %d, %Y')}\n"
        f"Description: {result.get('overview')}\n"
        )
        i += 1
    while True:
        choice = input("Please enter the ID of the show you want to add: ")
        if choice.isdigit() and 1 <= int(choice) <= len(response['results']):
            add_to_database = input("Would you like to save this show? (Y/N): ")
            if (add_to_database.lower() == "y"):
                data_to_add.append(
                    [
                        response['results'][int(choice) - 1].get("id"),
                        response['results'][int(choice) - 1].get("name"),
                        response['results'][int(choice) - 1].get("overview"),
                        response['results'][int(choice) - 1].get("first_air_date"),
                        response['results'][int(choice) - 1].get("vote_average")
                    ]
                )
            elif (add_to_database.lower() == "n"):
                break
            else:
                print("Please type (Y/N)")
                continue
        else:
            continue
        
        add_another = input("Would you like to add another show from the list? (Y/N): ")
        if (add_another.lower() == "y"):
            continue
        elif(add_another.lower() == "n"):
            return data_to_add
        else:
            return None

def display_game_information_found(response):
    data_to_add = []
    i = 1
    for result in response:
        unix_time_stamp = result.get("first_release_date")
        release_date = convert_release_date(unix_time_stamp)
        print(
        f"ID: {i}\n"
        f"Name: {result.get("name")}\n"
        f"Release Date: {release_date}\n"
        f"Description: {result.get("summary")}\n"
        )
        i += 1
    while True:
        choice = input("Please enter the ID of the game you want to add: ")
        if choice.isdigit() and 1 <= int(choice) <= len(response):
            add_to_database = input("Would you like to save this game? (Y/N): ")
            if (add_to_database.lower() == "y"):
                formatted_release_date = datetime.fromtimestamp(response[int(choice) - 1].get("first_release_date")).strftime("%Y-%m-%d")

                data_to_add.append(
                    [
                        response[int(choice) - 1].get("id"),
                        response[int(choice) - 1].get("name"),
                        response[int(choice) - 1].get("summary"),
                        formatted_release_date,
                        response[int(choice) - 1].get("rating"),
                    ]
                )
            elif (add_to_database.lower() == "n"):
                break
            else:
                continue

            add_another = input("Would you like to add another game from the list? (Y/N): ")
            if (add_another.lower() == "y"):
                continue
            elif (add_another.lower() == "n"):
                return data_to_add
            else:
                return None

def convert_release_date(unix_time_stamp):
    if unix_time_stamp is None:
        return "Unknown"
    else:
        return datetime.fromtimestamp(unix_time_stamp).strftime("%B %d, %Y")

def display_anime_information_found(response):
    data_to_add = []
    i = 1
    for result in response['data']['Page']['media']:
        title_dict = result.get("title")
        title = title_dict['english']

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
        else:
            release_date = ""
            
        print(
        f"ID: {i}\n"
        f"Name: {title}\n"
        f"Release Date: {release_date}\n"
        f"Description: {result.get("description")}\n"    
        )
        i += 1
    while True:
        choice = input("Please enter the id of the anime you want to add: ")
        media = response["data"]["Page"]["media"]

        if choice.isdigit() and 1 <= int(choice) <= len(media):
            add_to_database = input("Would you like to save this anime? (Y/N): ")
            if (add_to_database.lower() == "y"):
                chosen_title_dict = media[int(choice) - 1].get("title")
                chosen_title = chosen_title_dict['english']
        
                chosen_release_date_dict = media[int(choice) - 1].get("startDate")
                if chosen_release_date_dict is None:
                    chosen_release_date = ""
                else:
                    chosen_release_date = date(
                        chosen_release_date_dict['year'],
                        chosen_release_date_dict['month'],
                        chosen_release_date_dict['day']
                    )

                data_to_add.append(
                    [
                        media[int(choice) - 1].get("id"),
                        chosen_title,
                        media[int(choice) - 1].get("description"),
                        chosen_release_date,
                        media[int(choice) - 1].get("averageScore"),
                    ]
                )
            elif (add_to_database.lower() == "n"):
                break
            else:
                continue

            add_another = input("Would you like to add another anime from the list? (Y/N): ")
            if (add_another.lower() == "y"):
                continue
            elif (add_another.lower() == "n"):
                return data_to_add
            else:
                return None

def display_manga_information_found(response):
    data_to_add = []
    i = 1
    for result in response['data']['Page']['media']:
        title_dict = result.get("title")
        title = title_dict['english']

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
        else:
            release_date = ""
            
        print(
        f"ID: {i}\n"
        f"Name: {title}\n"
        f"Release Date: {release_date}\n"
        f"Description: {result.get("description")}\n"    
        )
        i += 1
    while True:
        choice = input("Please enter the id of the manga you want to add: ")
        if choice.isdigit() and 1 <= int(choice) <= len(response):
            add_to_database = input("Would you like to save this manga? (Y/N): ")
            if (add_to_database.lower() == "y"):
                chosen_title_dict = response['data']['Page']['media'][int(choice) - 1].get("title")
                chosen_title = chosen_title_dict['english']
        
                chosen_release_date_dict = response['data']['Page']['media'][int(choice) - 1].get("startDate")
                if chosen_release_date_dict is None:
                    chosen_release_date = ""
                else:
                    chosen_release_date = date(
                        chosen_release_date_dict['year'],
                        chosen_release_date_dict['month'],
                        chosen_release_date_dict['day']
                    )

                data_to_add.append(
                    [
                        response['data']['Page']['media'][int(choice) - 1].get("id"),
                        chosen_title,
                        response['data']['Page']['media'][int(choice) - 1].get("description"),
                        chosen_release_date,
                        response['data']['Page']['media'][int(choice) - 1].get("averageScore"),
                    ]
                )
            elif (add_to_database.lower() == "n"):
                break
            else:
                continue

            add_another = input("Would you like to add another manga from the list? (Y/N): ")
            if (add_another.lower() == "y"):
                continue
            elif (add_another.lower() == "n"):
                return data_to_add
            else:
                return None