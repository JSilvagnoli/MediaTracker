import sqlite3

con = sqlite3.connect("media_tracker.db")
cur = con.cursor()

def create_movie_database():
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
    
def create_show_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS shows (
            id INTEGER,
            name TEXT,
            overview TEXT,
            first_air_date TEXT,
            vote_average REAL
        )
    """)

def create_game_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER,
            name TEXT,
            summary TEXT,
            first_release_date TEXT,
            rating REAL
        )
    """)

def create_anime_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER,
            title TEXT,
            description TEXT,
            startDate TEXT,
            averageScore REAL
        )
    """)

def create_manga_database():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS manga (
            id INTEGER,
            title TEXT,
            description TEXT,
            startDate TEXT,
            averageScore REAL
        )
    """)

def add_movie_to_database(response):
    cur.executemany("""
        INSERT INTO movies VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def add_show_to_database(response):
    cur.executemany("""
        INSERT INTO shows VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def add_game_to_database(response):
    cur.executemany("""
        INSERT INTO games VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def add_anime_to_database(response):
    cur.executemany("""
        INSERT INTO anime VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def add_manga_to_database(response):
    cur.executemany("""
        INSERT INTO manga VALUES(?, ?, ?, ?, ?)""", response
    )
    con.commit()

def display_movie_database():
    cur.execute("SELECT * FROM movies")
    results = cur.fetchall()

    for movie in results:
        print(movie)
        
def display_show_database():
    cur.execute("SELECT * FROM shows")
    results = cur.fetchall()
    
    for show in results:
        print(show)

def display_game_database():
    cur.execute("SELECT * FROM games")
    results = cur.fetchall()

    for game in results:
        print(game)

def display_anime_database():
    cur.execute("SELECT * FROM anime")
    results = cur.fetchall()

    for anime in results:
        print(anime)

def display_manga_database():
    cur.execute("SELECT * FROM manga")
    results = cur.fetchall()

    for manga in results:
        print(manga)