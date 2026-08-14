import sqlite3

def create_database(type):
    con = sqlite3.connect("media_tracker.db")
    cur = con.cursor()

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {type} (
            id INTEGER PRIMARY KEY UNIQUE,
            title TEXT,
            description TEXT,
            release_date TEXT,
            rating REAL,
            image TEXT,
            type TEXT
        )
    """)

    con.commit()
    con.close()

def add_to_database(response):
    con = sqlite3.connect("media_tracker.db")
    cur = con.cursor()

    try:
        cur.execute(f"""
            INSERT INTO {response.get("type")} (id, title, description, release_date, rating, image, type) VALUES (:id, :title, :description, :releaseDate, :rating, :image, :type)""", response
        )
    except (sqlite3.Error, Exception) as e:
        print(f"Database error occured. Possibly Duplicate entry. Duplicate entries are not allowed")

    con.commit()
    con.close()

def display_database(type):
    con = sqlite3.connect("media_tracker.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute(f"SELECT * FROM {type}")
    results_dict = [dict(row) for row in cur.fetchall()]

    con.close()

    return results_dict