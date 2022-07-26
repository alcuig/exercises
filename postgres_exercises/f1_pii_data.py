import csv
import psycopg2
import uuid

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
table_name = "drivers_pii"
drop_table_sql = f"drop table if exists {table_schema}.{table_name}"

create_table_sql = f"""
    create table f1.drivers_pii (
        driver_forename varchar(50), 
        driver_surname varchar(50), 
        driver_dob varchar(50), 
        driver_nationality varchar(50),
        id  varchar(50),

        foreign key (id) references f1.simple_data_drivers(id)
        );
"""

create_table_sql = f"""
    create table f1.drivers_pii (
        driver_forename varchar(50), 
        driver_surname varchar(50), 
        driver_dob varchar(50), 
        driver_nationality varchar(50),
        id varchar(50) references f1.simple_data_drivers(id)
        );
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

# print(data)


# # iterate over the data, create the sql string that is to be executed by the database
# # execute the sql string
# # commit after the iteration has finished

#insert data into database via sql strings
print('inserting data')
for record in data: 

    postgres_insert_query = f""" 
        INSERT INTO {table_schema}.{table_name} (
            driver_forename, 
            driver_surname, 
            driver_dob, 
            driver_nationality
            )
    """
    
    record_to_insert = (
        record["driver_forename"],
        record["driver_surname"],
        record["driver_dob"],
        record["driver_nationality"]
        #str(uuid.uuid4())
    )
    print(postgres_insert_query)
    print(record_to_insert)

    cur.execute(postgres_insert_query, record_to_insert)

conn.commit()
count = cur.rowcount
print(count, "Record inserted successfully into mobile table")