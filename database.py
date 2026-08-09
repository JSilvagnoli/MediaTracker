import sqlite3

con = sqlite3.connect("media_tracker.db")
cur = con.cursor()

def create_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER,
            title TEXT,
            overview TEXT,
            release_date TEXT,
            vote_average REAL
        )
    """)

    con.commit()

def add_to_database(response):
    cur.execute("""
        INSERT INTO movies VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def display_database():
    cur.execute("SELECT * FROM movies")
    results = cur.fetchall()

    for movie in results:
        print(movie)