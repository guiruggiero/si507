# Developed by Gui Ruggiero

import sqlite3
import csv
import json

# Part 1: Read data from CSV and JSON into a new database called choc.db
DBNAME = "choc.db"
BARSCSV = "flavors_of_cacao_cleaned.csv"
COUNTRIESJSON = "countries.json"

# Reading JSON
with open(COUNTRIESJSON) as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    # print(json_data[0])

alpha2 = []
alpha3 = []
name = []
region = []
subregion = []
population = []
area = []

# i = 0
for country in json_data:
    # print(country)
    alpha2.append(country["alpha2Code"])
    alpha3.append(country["alpha3Code"])
    name.append(country["name"])
    region.append(country["region"])
    subregion.append(country["subregion"])
    population.append(country["population"])
    area.append(country["area"])
    # i += 1

# print(i) # 250
# print(alpha2)
# print(len(alpha2))
# print(area)
# print(len(alpha2))

# Reading CSV
csv_file = open(BARSCSV)
csv_data = csv.reader(csv_file)
# print(csv_data)

company = []
bean_name = []
ref = []
review = []
cocoa = []
location = []
rating = []
bean_type = []
bean_origin = []

# i = 0
for row in csv_data:
    # print(row)
    if row[0] != "Company":
        company.append(row[0])
        bean_name.append(row[1])
        ref.append(row[2])
        review.append(row[3])
        cocoa.append(row[4])
        location.append(row[5])
        rating.append(row[6])
        bean_type.append(row[7])
        bean_origin.append(row[8])
        # i += 1

# print(i) # 1795
# i = 0
# print(company[i])
# print(bean_name[i])
# print(ref[i])
# print(review[i])
# print(cocoa[i])
# print(location[i])
# print(rating[i])
# print(bean_type[i])
# print(bean_origin[i])

# Creating DB
conn = sqlite3.connect(DBNAME)
cur = conn.cursor()

# Dropping tables
statement = "DROP TABLE IF EXISTS 'Countries';"
cur.execute(statement)
# print("Table 'Countries' dropped (if existed)")

statement = "DROP TABLE IF EXISTS 'Bars';"
cur.execute(statement)
# print("Table 'Bars' dropped (if existed)")

conn.commit()

# Creating tables
statement = """
    CREATE TABLE 'Countries' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Alpha2' TEXT,
        'Alpha3' TEXT,
        'EnglishName' TEXT,
        'Region' TEXT,
        'Subregion' TEXT,
        'Population' INTEGER,
        'Area' REAL
    );
"""
cur.execute(statement)
# print("Table 'Countries' created")

statement = """
    CREATE TABLE 'Bars' (
        'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'Company' TEXT,
        'SpecificBeanBarName' TEXT,
        'REF' TEXT,
        'ReviewDate' TEXT,
        'CocoaPercent' REAL,
        'CompanyLocationId' INTEGER,
        'Rating' REAL,
        'BeanType' TEXT,
        'BroadBeanOriginId' INTEGER,
        FOREIGN KEY(CompanyLocationId) REFERENCES Countries(Id),
        FOREIGN KEY(BroadBeanOriginId) REFERENCES Countries(Id)
    );
"""
cur.execute(statement)
# print("Table 'Bars' created")

conn.commit()

# Inserting data into database
i = 0
for n in name:
    insertion = (None, alpha2[i], alpha3[i], name[i], region[i], subregion[i], population[i], area[i])
    statement = 'INSERT INTO "Countries" '
    statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cur.execute(statement, insertion)
    i += 1
conn.commit()
# print(i)

i = 0
for b in bean_name:
    # print(location[i])
    statement = "SELECT Id "
    statement += "FROM Countries "
    statement += "WHERE EnglishName = '" + location[i] + "'"
    # print(statement)
    cur.execute(statement)
    for row in cur:
        # print(row)
        location_id = int(row[0])
        # print(location_id)

    # print(bean_origin[i])
    statement = "SELECT Id "
    statement += "FROM Countries "
    statement += "WHERE EnglishName = '" + bean_origin[i] + "'"
    # print(statement)
    cur.execute(statement)
#    for row in cur:
        # print(row)
#        bean_origin_id = int(row[0])
        # print(bean_origin_id)

#     insertion = (None, company[i], bean_name[i], ref[i], review[i], cocoa[i], location_id, rating[i], bean_type[i], bean_origin_id)
#     statement = 'INSERT INTO "Bars" '
#     statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
#     cur.execute(statement, insertion)
    i += 1
# conn.commit()
print(i)

# # Part 2: Implement logic to process user commands
# def load_help_text():
#     with open("help.txt") as f:
#         # contents = f.read()
#         # print(contents)
#         return f.read()

# def process_command(command):
#     # aaa
#     return ()

# # Part 3: Implement interactive prompt. We've started for you!
# def interactive_prompt():
#     help_text = load_help_text()
#     # print(help_text)
#     response = ""
#     while response != "exit":
#         response = input("Enter a command: ")
#         query = process_command(response.strip())
#         # run SELECT ...

#         if response == "help":
#             print(help_text)
#             continue

# # Only runs when this file is run directly
# if __name__=="__main__":
#     # interactive_prompt()
#     pass