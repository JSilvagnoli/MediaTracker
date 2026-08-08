import ui
import tmdb

# JSONPlaceholderAPI testing
'''def main():
    url = 'https://jsonplaceholder.typicode.com'
    #get_example(url)
    #post_example(url)
    #put_example(url)
    #patch_example(url)
    delete_example(url)

def get_example(url):
    # GET Request: Fetch a single post by ID
    print("--- Get Request ---")
    response = requests.get(f"{url}/posts")

    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")

        for result in data:
            print(f"{result}\n")
    else:
        print(f"Failed to fetch data: {response.status_code}")

def post_example(url):
    # POST Request: Create a new post
    print("--- POST Request ---")
    new_post = {
        'userId': '11',
        'id': '101',
        'title': 'Study Python',
        'body': 'I plan to study Python to build up the skills necessary to get hired as a junior python developer.'
    }
    response = requests.post(f"{url}/posts", json=new_post)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def put_example(url):
    # PUT Request: Update an existing post
    print("--- PUT Request ---")
    response = requests.get(f"{url}/posts/1")
    original_post = response.json()
    print(f"Original Post: {original_post}")
    
    updated_post = {
        'userId': 5000,
        'id': 9999,
        'title': 'Wash Car',
        'body': 'I really need to wash my car later'
    }
    response = requests.put(f"{url}/posts/1", json=updated_post)
    print(f"Status Code: {response.status_code}")
    print(f"Updated Response: {response.json()}")

def patch_example(url):
    # PATCH Request: Update a portion of an existing post
    print("--- PATCH ---")
    response = requests.get(f"{url}/posts/1")
    original_post = response.json()
    print(f"Original Post: {original_post}")
    updated_portion = {
        'id': 1234
    }
    response = requests.patch(f"{url}/posts/1", json=updated_portion)
    print(f"Status Code: {response.status_code}")
    print(f"Updated Post: {response.json()}")

def delete_example(url):
    # DELETE Request: Delete an existing post
    print("--- DELETE ---")
    post_to_delete = {
        'id': 1
    }
    response = requests.delete(f"{url}/posts/1", json=post_to_delete)
    print(f"Status Code: {response.status_code}")'''

def main():
    handle_menu_choice(ui.display_menu())

def handle_menu_choice(user_input):
    handler = MENU_CHOICES.get(user_input)
    if handler:
        handler()

def handle_get_movie_title():
    movie_to_find = ui.get_movie_title()
    response = tmdb.get_movie_information(movie_to_find)
    ui.display_movie_title(response)

def handle_get_movie_information():
    movie_to_find = ui.get_movie_information()
    response = tmdb.get_movie_information(movie_to_find)
    ui.display_movie_information(response)

MENU_CHOICES = {
    '1': handle_get_movie_title,
    '2': handle_get_movie_information
}

if __name__ == "__main__":
    main()