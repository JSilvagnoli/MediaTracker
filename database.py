import sqlite3
from datetime import datetime, date

con = sqlite3.connect("media_tracker.db")
cur = con.cursor()

def create_database(type):
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {type} (
            id INTEGER,
            title TEXT,
            description TEXT,
            release_date TEXT,
            rating REAL,
            type TEXT
        )
    """)

    con.commit()

def add_to_database(response):
    cur.execute(f"""
        INSERT INTO {response.get("type")} (id, title, description, release_date, rating, type) VALUES (:id, :title, :description, :release_date, :rating, :type)""", response
    )

    con.commit()

def display_database(type):
    cur.execute(f"SELECT * FROM {type}")
    results = cur.fetchall()

    for result in results:
        print(result)