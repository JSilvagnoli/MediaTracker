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
        user_input = input("What would you like to do? (Enter 1, 2, 3, ...): ")
        match user_input:
            case "1":
                return "movie"
            case "2":
                return "show"
            case "3":
                return "game"
            case "4":
                return "anime"
            case "5":
                return "manga"
            case _:
                print("Please enter a valid option.")

def get_media_name():
    return input("Please enter the name of the media you want to search for or leave blank to return to menu: ")

def display_information_found(response):
    i = 1
    for result in response:
        release_date = result.get("release_date")
        if release_date != "No Release Date Available":
            release_date = datetime.fromisoformat(release_date).strftime("%B %d, %Y")
        print(
        f"ID: {i}\n"
        f"Name: {result.get("title")}\n"
        f"Release Date: {release_date}\n"
        f"Description: {result.get("description")}\n"
        )
        i += 1

def select_media(response):
    while True:
        choice = input("Please enter the ID of the media you want to add or leave blank to return to menu: ")

        if choice.isdigit() and 1 <= int(choice) <= len(response):
            return response[int(choice) - 1]
        elif choice == "":
            return None
        else:
            print("Please enter a valid ID or leave blank to return to menu.")

def confirm(prompt):
    while True:
        answer = input(f"{prompt} (Y/N): ").strip().lower()

        if answer in ("y", "n"):
            return answer == "y"

        print("Please type Y or N.")