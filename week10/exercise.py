import sqlite3
import csv

# Initializing SQLite connector
conn = sqlite3.connect('airport_data.sqlite')
cur = conn.cursor()

# Dropping tables
statement = '''
    DROP TABLE IF EXISTS 'Airport';
'''
cur.execute(statement)
# print("\nTable 'Airport' dropped (if existed)")

statement = '''
    DROP TABLE IF EXISTS 'City';
'''
cur.execute(statement)
# print("Table 'City' dropped (if existed)")

statement = '''
    DROP TABLE IF EXISTS 'State';
'''
cur.execute(statement)
# print("Table 'State' dropped (if existed)")

statement = '''
    DROP TABLE IF EXISTS 'Country';
'''
cur.execute(statement)
# print("Table 'Country' dropped (if existed)")

conn.commit()

# Creating tables
statement = '''
    CREATE TABLE 'Country' (
        'country_id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'country_name' TEXT NOT NULL,
    );
'''
cur.execute(statement)
# print("Table 'Country' created")

statement = '''
    CREATE TABLE 'State' (
        'state_id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'state_abbrev' TEXT NOT NULL,
        'country_id' INTEGER,
        FOREIGN KEY(country_id) REFERENCES Country(country_id),
    );
'''
cur.execute(statement)
# print("Table 'State' created")

statement = '''
    CREATE TABLE 'City' (
        'city_id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'city_name' TEXT NOT NULL,
        'state_id' INTEGER,
        FOREIGN KEY(state_id) REFERENCES State(state_id),
        'country_id' INTEGER,
        FOREIGN KEY(country_id) REFERENCES Country(country_id),
    );
'''
cur.execute(statement)
# print("Table 'City' created")

statement = '''
    CREATE TABLE 'Airport' (
        'airport_id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'iata' TEXT NOT NULL,
        'airport_name' TEXT NOT NULL,
        'lat' REAL,
        'long' REAL,
        'city_id' INTEGER,
        FOREIGN KEY(city_id) REFERENCES City(city_id),
        'traffic' INTEGER,
    );
'''
cur.execute(statement)
# print("Table 'Airport' created")

conn.commit()

# Reading CSV
f = open('2011_february_us_airport_traffic.csv')
csv_data = csv.reader(f)

iata = []
airport = []
city = []
state = []
country = []
lat = []
lgn = []
traffic = []

for row in csv_data:
    if row[0] != 'iata':
        iata.append(row[0])
        airport.append(row[1])
        city.append(row[2])
        state.append(row[3])
        country.append(row[4])
        lat.append(row[5])
        lgn.append(row[6])
        traffic.append(row[7])

# i = 0
# print(iata[i])
# print(airport[i])
# print(city[i])
# print(state[i])
# print(country[i])
# print(lat[i])
# print(lgn[i])
# print(traffic[i])

# Inserting data into database
# Table 'Country'
i = 0
for c in country:
    insertion = (None, country[i])
    statement = 'INSERT INTO "Countries" '
    statement += 'VALUES (?, ?)'
    cur.execute(statement, insertion)
    i += 1

# Table 'State'
i = 0
for s in state:
    insertion = (None, state[i], "...") # flag
    statement = 'INSERT INTO "State" '
    statement += 'VALUES (?, ?, ?)'
    cur.execute(statement, insertion)
    i += 1

# Table 'City'
i = 0
for c in city:
    insertion = (None, city[i], "state ...", "country...") # flag
    statement = 'INSERT INTO "City" '
    statement += 'VALUES (?, ?, ?, ?)'
    cur.execute(statement, insertion)
    i += 1

# Table 'Airport'
i = 0
for a in airport:
    insertion = (None, iata[i], airport[i], lat[i], lgn[i], "city ...", traffic[i]) # flag
    statement = 'INSERT INTO "Airport" '
    statement += 'VALUES (?, ?, ?, ?, ?, ?, ?)'
    cur.execute(statement, insertion)
    i += 1

conn.commit()

# Updating DTW data
new_taffic = 8500
airport_code = 'DTW'

update = (new_taffic, airport_code)
statement = 'UPDATE Airport '
statement += 'SET traffic = ? '
statement += 'WHERE iata = ?'

# print(statement)
cur.execute(statement)

conn.commit()

# Performing asked query
statement = "SELECT Airport.iata, City.city_name, Airport.traffic "
statement += "FROM Airport JOIN City ON Airport.city_id = City.city_id "
statement += "JOIN State ON City.state_id = State.state_id "
statement += "WHERE State.state_abbrev = 'MI'"

cur.execute(statement)
# for row in cur:
#     print(row)

conn.close()