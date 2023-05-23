from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_database.sqlite3', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Competition(Base):
    __tablename__ = 'competition'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
    date = Column(Integer)
    location = Column(String(20))

    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location

    def __repr__(self):
        return f'Competition:{self.name}, date:{self.date}, City:{self.location}'


class Sportsman(Base):
    __tablename__ = 'sportsman'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
    birth_year = Column(Integer)

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f'Sportsman:{self.name}, birth_year:{self.birth_year}'


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    competition_id = Column(Integer(), ForeignKey('competition.id'))
    sportsman_id = Column(Integer(), ForeignKey('sportsman.id'))
    world_record = Column(Integer)
    personal_record = Column(Integer)

    def __init__(self, competition_id, sportsman_id, world_record, personal_record):
        self.competition_id = competition_id
        self.sportsman_id = sportsman_id
        self.world_record = world_record
        self.personal_record = personal_record

    def __repr__(self):
        return


Base.metadata.create_all(engine)
session = Session()

comp = Competition('Olympic Games', 23-07.2021, 'Tokyo')
session.add(comp)
comp = Competition('World Championships', 15-05.2010, 'Madrid')
session.add(comp)
comp = Competition('European Cup', 12-05.2010, 'Berlin')
session.add(comp)
all_comp = session.query(Competition).all()
session.commit()

spm = Sportsman('Usain Bolt', 1986)
session.add(spm)
spm = Sportsman('Justin Gatlin', 1982)
session.add(spm)
spm = Sportsman('Tyson Gay', 1982)
session.add(spm)
spm = Sportsman('Asafa Powell', 1982)
session.add(spm)
spm = Sportsman('Yohan Blake', 1989)
session.add(spm)
spm = Sportsman('Christophe Lemaitre', 1990)
session.add(spm)
spm = Sportsman('Dwain Chambers', 1978)
session.add(spm)
spm = Sportsman('Richard Thompson', 1985)
session.add(spm)
all_spm = session.query(Sportsman).all()
session.commit()

res = Result(1, 1, 9.63, 9.64)
session.add(res)
res = Result(1, 2, 9.87, 9.84)
session.add(res)
res = Result(2, 3, 10.12, 10.15)
session.add(res)
res = Result(2, 4, 10.20, 10.20)
session.add(res)
res = Result(2, 5, 10.22, 10.25)
session.add(res)
res = Result(3, 6, 9.94, 10.01)
session.add(res)
res = Result(3, 7, 10.02, 10.03)
session.add(res)
res = Result(3, 8, 10.15, 10.12)
session.add(res)
all_res = session.query(Result).all()
session.commit()
