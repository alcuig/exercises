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
table_name = "f1_data"
drop_table_sql = f"drop table if exists {table_schema}.{table_name}"

create_table_sql = f"""
    create table {table_schema}.{table_name} (
        id varchar(50) primary key, 
        driverRef varchar(50),
        driver_number int, 
        driver_code varchar(50), 
        driver_forename varchar(50), 
        driver_surname varchar(50), 
        driver_dob varchar(50), 
        driver_nationality varchar(50),
        points numeric,
        fastestLapTime varchar(50)
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


# # iterate over the data, create the sql string that is to be executed by the database
# # execute the sql string
# # commit after the iteration has finished

#insert data into database via sql strings

for record in data: 

    postgres_insert_query = f""" 
        INSERT INTO {table_schema}.{table_name} (
            id, 
            driverRef,
            driver_number, 
            driver_code, 
            driver_forename, 
            driver_surname, 
            driver_dob, 
            driver_nationality,
            points,
            fastestLapTime)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    if 'N' in record["driver_number"]:
        record["driver_number"] = None


    record_to_insert = (
        str(uuid.uuid4()),
        record["driverRef"],
        record["driver_number"],
        record["driver_code"],
        record["driver_forename"],
        record["driver_surname"],
        record["driver_dob"],
        record["driver_nationality"],
        record["points"],
        record["fastestLapTime"],
    )

    cur.execute(postgres_insert_query, record_to_insert)

conn.commit()
count = cur.rowcount
print(count, "Record inserted successfully into mobile table")

#----------------------


#insert new column age

#find nationality, date of birth and name of person with fastest lap time
#select fastestLapTime, driver_surname, driver_nationality from f1.f1_data order by fastestLapTime tb limit 1;
#selects columns I want to see from the table, ranks them according to the order of fastestlaptime, slices the 1st result (which will be smallest) 

#find out who is the youngest driver
#(select driver_dob, driver_surname, driver_forename from f1.f1_data order by driver_dob desc)limit 1;

#select distinct driver names, distinct driver births dates, distinct driver codes

#find all british drivers (where nationality = 'British')


#use NOT to show drivers who aren't british (where not nationality = 'british')
#select distinct driver_nationality from f1.f1_data where not driver_nationality = 'British' order by driver_nationality;

#select all records where driver is British AND is older than 30
#select distinct driver_nationality, driver_dob from f1.f1_data where not driver_nationality = 'British' and driver_dob ~ '19[0-9][012]' order by driver_dob desc;

#select all records where the driver is japanese or french
#select distinct driver_surname, driver_nationality from f1.f1_data where driver_nationality = 'French'
# or driver_nationality = 'Japanese' order by driver_nationality, driver_surname desc;

# select all records where the driver is older than 31 or younger than 25
#???

#Order the records alphabetically by nationality
#select distinct driver_surname, driver_nationality from f1.f1_data order by driver_nationality, driver_surname;

# order records by youngest to eldest
#select distinct driver_surname, driver_forename, driver_dob from f1.f1_data order by driver_dob desc;


#Order records alphabetically by nationality then by race lap 
#select distinct driver_surname, driver_forename, driver_nationality, fastestLapTime from f1.f1_data order by driver_nationality, fastestLapTime;

#insert a new record into the table , if you are inserting values into all columns in the table you do not need to specify column headers
#INSERT INTO table_name
#VALUES (value1, value2, value3, ...);
#insert into f1.f1_data values ('000', 'DriverName', 0001, 'TEST', 'Imnot', 'Arealdriver', '2022-01-01', 'Avatarian', 900, '01:27.09');

#select all records where the driver number is empty where X IS NULL, and then all those where the driver number is not empty
#select distinct driver_number, driver_forename, driver_surname from f1.f1_data where driver_number is null;
#select distinct driver_number, driver_forename, driver_surname from f1.f1_data where driver_number is not null order by driver_number;


#find driver code of oldest driver
#select distinct driver_code, driver_dob from f1.f1_data where driver_code not like '%\N%'  order by driver_dob;


#UPDATE/ SET command : update the Nationality column of all drivers who have a P in their surname to french
#update f1.f1_data set driver_nationality = 'French' where driver_surname like '%p%';

#count the number of drivers who now have the french nationality
#select count (distinct driver_dob) from f1.f1_data where driver_nationality = 'French';

#set the value of all surname columns to NotFrench, but only where the nationality column is not french (update, set where)
#update f1.f1_data set driver_surname = 'NotFrench' where driver_nationality != 'French';

#where nationality is british and firstname is George, set surname to "Orwell"
# update f1.f1_data set driver_surname = 'Orwell' where driver_forename = 'George' and driver_nationality = 'British';

#delete all records whose driver code is "HAM" (delete from table where X = X)


#delete all the recrods from the table (delete from table_name)

#Use the MIN function (Min(ColumnName)) to select the minimum value from the lap time


#Use Max function to select max value from lap time

#use count function to return the number of records that have the code value set to HAM
#select count(driver_code) from f1.f1_data where driver_code = 'HAM';

#calculate average of all points AVG(column)


#calculate sum of all points select SUM(Column) from TableName;


#like function to find records where last name column starts with "R"


#Select * from Table where Column LIKE 'letter%';
#select sum(points) as SumPoints from f1.f1_data;


#select all records where first name sztarts with G and ends with e
#select distinct driver_surname, driver_forename from f1.f1_data where driver_forename like 'G%e';


#select all records where first name does not start with L
#select distinct driver_surname, driver_forename from f1.f1_data where driver_forename not like 'L%';


#select all records where second letter first name is E ('_e%)


#select all records where the driver_forename begins with the letters A, S or L
#select distinct driver_surname, driver_forename from f1.f1_data where driver_forename ~ '^[ASL]';

# select all records where last name begins with anything from L to Y '[a-f]
#select distinct driver_surname, driver_forename from f1.f1_data where driver_surname ~* '^[l-y]';

# #select all records where first letter of nationality is not B or F or C '[!bfc]
#select distinct driver_surname, driver_forename, driver_nationality from f1.f1_data where driver_nationality !~* '^[bfc]';

#----
#use IN operator to select all records where name is either George or Mick
#The IN operator allows you to specify multiple values in a WHERE clause.
#The IN operator is a shorthand for multiple OR conditions.

#IN Syntax
#SELECT column_name(s)
#FROM table_name
#WHERE column_name IN (value1, value2, ...);

#select distinct driver_forename, driver_surname, driver_code, driver_dob from f1.f1_data where driver_forename in ('George', 'Mick') order by driver_dob;
#---

#use IN operator to select all records where name is neither Paul nor Pierre nor Lewis, nor Max;
#select from TableName WHERE ColumnName NOT IN('Condition1','Condition2');
#select distinct driver_surname, driver_forename, driver_dob, driver_nationality from f1.f1_data where driver_forename not in ('Paul', 'Lewis', 'Pierre', 'Max') order by driver_dob;

#-----
#BETWEEN 

#find people whose DOBS are beteween 1989 and 1999 
# #syntax : (select from Table WHERE column BETWEEN x AND x)

#select * from f1.f1_data where driver_dob between '1989-01-01' and '1999-01-01';


#-----
#show records where values of first name are alphabetically between Geoorge and Mick 
# Select * from TableName where ColumnName BETWEEN 'x' AND 'x'
#select driver_forename, driver_surname, driver_dob from f1.f1_data as NewDriverTable where driver_forename between 'George' and 'Mick';

#---
#IS NOT BETWEEN
##find all records where points are NOT in between 10 and 8;
#select * from f1.f1_data where points not between 8 and 10 order by points desc;

#---
#AVG
#find which driver has highest average points
#???

#---
#SQL alias (to give temporary name to table column)
#Select ColumnName, ColumnName2, ColumnName3 AS AliasName, FROM TableName;
#select driverref, driver_dob, driver_nationality from f1.f1_data as NewDriverTable;

#-----


#transform racetime into seconds
#average fastest seconds per driver
#insert other columns
#find out who was in first position most often


#when displaying the f1 table, refer to the table as formula 1 instead of f1
#Select * from TableName AS AliasName,
#select * from f1.f1_data as formula_1_data

#---
#JOIN 

#create table with all drivers - name, surname, and create a surrogate key  (i.e. UUID). Make UUID the primary key.
#create table with all the PII(DOB, nationality etc) of the driver, from the first task get the surrogate key  as a foreign key in this table
# create table with all the races and drivers in the race.

#TO LEFT JOIN : Select * FROM TableName1 LEFT JOIN Table2 ON TableName1.PrimaryKey = TableName2.SameKey;

#Select all records from the two tables where there is a match in both tables.

#SELECT * FROM Table1 INNER JOIN Table2 ON TableName1.PrimaryKey = TableName2.SameKey


#RIGHT JOIN clause to select all the records from one table plus all the matches in a second table.

#Group By
#List the numbers of drivers of each nationality
#Select COUNT(DriverName), Nationality FROM TableName GROUP BY Nationality;

#--
#CREATE DATABASE
#Create a new database 
#CREATE DATABASE newDB;

#Delete database
#DROP DATABASE newDB;

#create table (will need to indicate column headers plus datatype)
#drop the table

#delete all data in table but not table itself 

#add a column of type DATE called Birthday (ALTER TABLE)

#drop driver code column from table