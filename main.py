import sqlite3

import ui
import tmdb
import database

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
    # Setting up SQLite
    '''con = sqlite3.connect("media_tracker.db")

    # Execute SQL statements and fetch results from SQL queries
    cur = con.cursor()

    # Create database table movie with columns for title, release year, and review score. For simplicity, you can use column names in the table declaration
    cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

    # Verify that the new table has been created by querying the sqlite_master table built-in to SQLite
    res = cur.execute("SELECT name FROM sqlite_master")
    res.fetchone()

    # Query non-existent table spam
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    res.fetchone() is None

    # Add two rows of data using INSERT
    cur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)

    # INSERT opens a transaction, which needs to be committed before changes are saved in the database
    con.commit()

    # Verify the data was inserted correctly
    res = cur.execute("SELECT score FROM movie")
    res.fetchall()

    # Insert 3 more rows calling cur.executemany()
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()

    # Verify the new rows were inserted by executing a SELECT query and iterating over the results
    for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
        print(row)

    # Verify that the database has been written to disk
    con.close()
    # Verify that everything worked correctly
    new_con = sqlite3.connect("media_tracker.db")
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
    title, year = res.fetchone()
    print(f'The highest scoring Monty Python movie is {title!r}, released in {year}.')
    new_con.close()'''

    database.create_database()

    handle_menu_choice(ui.display_menu())

def handle_menu_choice(user_input):
    handler = MENU_CHOICES.get(user_input)
    if handler:
        handler()

def handle_get_movie_title():
    movie_to_find = ui.get_movie_title()
    response = tmdb.get_movie_information(movie_to_find)
    #ui.display_movie_title(response)
    selected_response = ui.select_movie_title(response)
    return selected_response

def handle_get_movie_information():
    movie_to_find = ui.get_movie_information()
    response = tmdb.get_movie_information(movie_to_find)
    selected_movie = ui.select_movie_title(response)
    handle_add_movie_to_database(selected_movie)
    database.display_database()

def select_specific_movie():
    response = ui.pick_movie()
    return response

def handle_add_movie_to_database(response):
    database.add_to_database(response)

MENU_CHOICES = {
    '1': handle_get_movie_title,
    '2': handle_get_movie_information
}

if __name__ == "__main__":
    main()