

def display_menu():
    print("=====================")
    print("    Media Tracker    ")
    print("=====================")

    print("---------------------")
    print("1. Get Movie Title")
    print("2. Get Movie Information")
    print()

    while True:
        user_input = input("What would you like to do? (Enter 1, 2, 3, 4, ...): ")
        if user_input in ("1", "2", "3", "4", "5"):
            return user_input

def get_movie_title():
    return input("Please enter the name of the movie you want to search for: ")

def get_movie_information():
    return input("Please enter the name of the movie you want information on: ")

def display_movie_title(response):
    data_to_display = []
    for result in response['results']:
        data_to_display.append([f"Title: {result.get("title")}"])
    for title in data_to_display:
        print(title)

def display_movie_information(response):
    data_to_display = []
    for result in response['results']:
        data_to_display.append([f"ID: {result.get("id")}", f"Title: {result.get("title")}", f"Description: {result.get("overview")}", f"Release Date: {result.get("release_date")}"])
    for info in data_to_display:
        print(info)

def select_movie_title(response):
    i = 1
    for result in response['results']:
        print("ID:" + str(i) + " " + result.get("title"))
        i += 1

    choice = input("Please enter the ID of the movie you want to add. ")
    data_to_add = [
        response['results'][int(choice) - 1].get("id"),
        response['results'][int(choice) - 1].get("title"),
        response['results'][int(choice) - 1].get("overview"),
        response['results'][int(choice) - 1].get("release_date"),
        response['results'][int(choice) - 1].get("vote_average"),
    ]
    print(data_to_add)
    return data_to_add