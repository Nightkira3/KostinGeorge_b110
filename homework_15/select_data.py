import sqlite3


with sqlite3.connect('db.sqlite3') as con:
    cur = con.cursor()

    cur.execute('''
    INSERT INTO competition(name, date, location)
    VALUES('Olympic Games', '23-07-2021', 'Tokyo');
    ''')

    cur.execute('''
    INSERT INTO competition(name, date, location)
    VALUES('World Championships', '15-05-2010', 'Madrid');
    ''')

    cur.execute('''
    INSERT INTO competition(name, date, location)
    VALUES('European Cup', '12-05-2010', 'Berlin');
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Usain Bolt', 1986);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Justin Gatlin', 1982);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Tyson Gay', 1982);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Asafa Powell', 1982);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Yohan Blake', 1989);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Christophe Lemaitre', 1990);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Dwain Chambers', 1978);
    ''')

    cur.execute('''
    INSERT INTO sportsman(name, birth_year)
    VALUES('Richard Thompson', 1985);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(1, 1, 9.63, 9.64);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(1, 2, 9.87, 9.84);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(2, 3, 10.12, 10.15);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(2, 4, 10.20, 10.20);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(2, 5, 10.22, 10.25);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(3, 6, 9.94, 10.01);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(3, 7, 10.02, 10.03);
    ''')

    cur.execute('''
    INSERT INTO result(competition_id, sportsman_id, world_record, personal_record)
    VALUES(3, 8, 10.15, 10.12);
    ''')

    con.commit()
