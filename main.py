from utils import *
from settings import *
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///clean_measure_and_stations.db', echo=True)
meta = MetaData()

clean_measure_db = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('date', String),
    Column('precip', String),
    Column('tobs', String),
)

clean_stations_db = Table(
    'clean_stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', String),
    Column('longitude', String),
    Column('elevation', String),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

meta.create_all(engine)
conn = engine.connect()

data_clean_measure = load_data_from_csv_file(file_clean_measure)
insert_clean_measure = clean_measure_db.insert()
conn.execute(insert_clean_measure, data_clean_measure)

data_clean_stations = load_data_from_csv_file(file_clean_stations)
insert_clean_stations = clean_stations_db.insert()
conn.execute(insert_clean_stations, data_clean_stations)

test_response = conn.execute("SELECT name, country, state FROM clean_stations LIMIT 10").fetchall()
print(test_response)