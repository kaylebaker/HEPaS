import sqlite3
import Pyro4
import pandas as pd

DB_DIR = "src\server-2\oust_database.db"
TABLES = ["Courses", "Students", "StudentUnits"]

# Look up server-1 in the name server
nameserver = Pyro4.locateNS()
uri = nameserver.lookup("server-2")

# Create a Proxy for server-2
server1 = Pyro4.Proxy(uri)

# Establish connection to SQLite database and create cursor object to perform SQL operations
conn = sqlite3.connect(DB_DIR)
cur = conn.cursor()



def displayDBSchema(table_name):
    schema_info = cur.execute(f"PRAGMA table_info({table_name})").fetchall()
    print(f"Schema details for table {table_name}:")
    for column in schema_info:
        print(f"Column: {column[1]}, Type: {column[2]}, Nullable: {column[3]}, Default: {column[4]}")
    print()


def displayStudentRecords():
    data = []
    for record in cur.execute('SELECT * FROM Students'):
        row_data = [record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]]
        data.append(row_data)

    df = pd.DataFrame(data, columns = ['student_id', 'fname', 'lname', 'email', 'mobile', 'course_code', 'units_attempted', 'units_completed', 'course_status'])

    print(df.to_string(index=False))


def addRecord(table_name, record):
    try:
        cur.execute(f'INSERT INTO {table_name} {record}')
        if cur.rowcount == 1:
            print("Record added successfully.")
        else:
            print("No record was inserted.")

    except Exception as e:
        print("ERROR: Unable to insert new record.", e)


def deleteRecord(table_name, identifier):
    field = ""
    if table_name == 'Courses':
        field = 'course_code'
    elif table_name == 'Students':
        field = 'student_id'
    else:
        print("ERROR")
        return
    
    try:
        cur.execute(f'DELETE FROM {table_name} WHERE {field}={identifier}')
        if cur.rowcount == 1:
            print("Record deleted successfully.")
        else:
            print("No record was deleted.")

    except Exception as e:
        print("ERROR: Unable to delete record.", e)


    print("----------------------------------")
    print("|    DATABASE INTERFACE CLIENT   |")
    print("----------------------------------\n")

while(True):
    print("1.\tDisplay table schema")
    print("2.\tDisplay student records")
    print("3.\tAdd a record")
    print("4.\tDelete a record")
    print("5.\tExit")

    print("> ", end="")
    selection = input()

    if selection == '1':
        for table in TABLES:
            displayDBSchema(table)

    elif selection == '2':
        displayStudentRecords()

    elif selection == '5':
        break

print("Goodbye")
input()
exit()

