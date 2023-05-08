import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS sportsman (
        id INTEGER PRIMARY KEY,
        name TEXT,
        birth_year INTEGER NOT NULL
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS competition (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date INTEGER NOT NULL,
        location TEXT 
    );
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY,
        competition_id INTEGER NOT NULL,
        sportsman_id  INTEGER NOT NULL,
        world_record  INTEGER NOT NULL,
        personal_record   INTEGER NOT NULL,
        FOREIGN KEY(competition_id) REFERENCES competition(id),
        FOREIGN KEY(sportsman_id) REFERENCES sportsman(id)
    );
    ''')

    con.commit()
