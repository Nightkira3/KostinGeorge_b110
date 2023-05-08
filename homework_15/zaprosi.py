# Выдать всю информацию о спортсменах из таблицы sportsman
    cur.execute('''
    SELECT * FROM sportsman;
    ''')

# Выдать наименование и мировые результаты по всем соревнованиям
    cur.execute('''
    SELECT competition.name, result.world_record FROM competition
    JOIN result ON competition.id = result.competition_id;
    ''')

# Выбрать имена всех спортсменов, которые родились в 1990 году
    cur.execute('''
    SELECT name FROM sportsman WHERE birth_year = 1990;
    ''')

# Выбрать наименование и мировые результаты по всем соревнованиям, установленные 12-05-2010 или 15-05-2010
    cur.execute('''
    SELECT competition.name, result.world_record FROM competition
    JOIN result ON competition.id = result.competition_id
    WHERE competition.date = '12-05-2010' OR competition.date = '15-05-2010';
    ''')

# Выбрать дату проведения всех соревнований, проводившихся в Москве и полученные на них результаты равны 10 секунд
    cur.execute('''
    SELECT competition.date FROM competition
    JOIN result ON competition.id = result.competition_id
    WHERE competition.location = 'Moscow' AND result.world_record = 10;
    ''')

# Выбрать имена всех спортсменов, у которых персональный рекорд менее 25 с
    cur.execute('''
    SELECT name FROM sportsman WHERE personal_record < 25;
    ''')