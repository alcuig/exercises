import csv
import psycopg2
import uuid
from pprint import pprint

header = []
rows = []
with open("drivers.csv", 'r') as file:
    csvreader = csv.reader(file) #use the csv.reader object to read the CSV file
    header = next(csvreader)
    for row in csvreader: #Extract the rows/records #Create an empty list called rows and iterate through the csvreader object and append each row to the rows list.
        rows.append(row)
#print(header)
# print(rows)

table_schema = "f1"
table_name = "drivers"
drop_table_sql = f"drop table if exists {table_schema}.{table_name}"

create_table_sql = f"""
    create table {table_schema}.{table_name} (
        driver_forename varchar(50), 
        driver_surname varchar(50),
        primary key (driver_forename, driver_surname)
    )
"""

conn = psycopg2.connect("host=localhost dbname=zoopla user=alyssacuignet")
cur = conn.cursor()
cur.execute(drop_table_sql)
cur.execute(create_table_sql)
conn.commit()

# # Reshape the data such that you have a list of dictionaries 
# # the data should look like [{'col1': val1, 'col2': val2}, {'col1': valX, 'col2': valY}, ...]


row = rows[0]
print(row)
print(header)
#spec_headers = ['driver_surname', 'driver_dob']
data = []

for row in rows:
    line = {}
    for i in range(len(header)):
        #if header[i] in spec_headers:
        line[header[i]] = row[i]
    data.append(line)

pprint(data[0:3])


# # iterate over the data, create the sql string that is to be executed by the database
# # execute the sql string
# # commit after the iteration has finished

#insert data into database via sql strings

# drivers_set = []


# for record in data: 
#     print(record)
#     print("----")

#     postgres_insert_query = f""" 
#         INSERT INTO {table_schema}.{table_name} (
#             driver_forename, 
#             driver_surname
#             )
#             VALUES (%s,%s)
#     """


#     record_to_insert = (
#         record["driver_forename"],
#         record["driver_surname"]
#     )

#     cur.execute(postgres_insert_query, record_to_insert)

# conn.commit()
# count = cur.rowcount
# print(count, "Driver names inserted successfully into mobile table")
