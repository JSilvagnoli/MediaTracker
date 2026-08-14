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
            type TEXT,
            favorite_status INTEGER DEFAULT 0
        )
    """)

    con.commit()
    con.close()

def add_to_database(response):
    con = sqlite3.connect("media_tracker.db")
    cur = con.cursor()

    print(response)
    try:
        cur.execute(f"""
            INSERT INTO {response.get("type")} (id, title, description, release_date, rating, image, type) VALUES (:id, :title, :description, :releaseDate, :rating, :image, :type)""", response
        )
    except sqlite3.Error as e:
        print(f"Database error occured. Possibly Duplicate entry. Duplicate entries are not allowed: {e}")

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

def update_favorite_status(data):
    con = sqlite3.connect("media_tracker.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute(
        f"UPDATE {data["type"]} SET favorite_status = ? WHERE id = ?",
        (data["favorite_status"], data["id"])
    )

    cur.execute(f"SELECT * FROM {data["type"]}")
    results_dict = [dict(row) for row in cur.fetchall()]
    print(results_dict)

    con.commit()
    con.close()

def display_favorites(favorite_status):
    con = sqlite3.connect("media_tracker.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute(f"SELECT * FROM {favorite_status} WHERE favorite_status = 1")
    results_dict = [dict(row) for row in cur.fetchall()]

    con.close()

    return results_dict