import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE COMPETITION (
        id INTEGER PRIMARY KEY,
        name NAME,
        date INTEGER NOT NULL,
        location INTEGER NOT NULL
        
    );
    ''')
