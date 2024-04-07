import Pyro4
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

DB_DIR = "src\server-2\oust_database.db"
TABLES = ["Courses", "Students", "StudentUnits"]
USER = os.getenv('DB_USERNAME')
PASS = os.getenv('DB_PASSWORD')

try:
    # Look up server-2 in the name server
    print("Looking up server-2 in Pyro name server...")
    nameserver = Pyro4.locateNS()
    uri = nameserver.lookup("server-2")

    # Create a Proxy for server-2
    server2 = Pyro4.Proxy(uri)
    print("Server located! Now connected to server-2.")

except Exception as e:
    print("Unable to connect to remote server", e)


print("----------------------------------")
print("|    DATABASE INTERFACE CLIENT   |")
print("----------------------------------\n")

attempts = 3
authorised = False
while (attempts != 0):
    print("Enter credentials to login.")
    print("Username: ", end="")
    username = input()
    print("Password: ", end="")
    password = input()

    if username == USER and password == PASS:
        authorised = True
        break
    else:
        attempts -= 1
        print(f"Invalid credentials. {attempts} attempts remaining.")

while(authorised == True):
    print("\nSelect from below menu options:")
    print(" 1.\tDisplay table schema")
    print(" 2.\tDisplay student records")
    print(" 3.\tAdd a record")
    print(" 4.\tDelete a record")
    print(" 5.\tExit")

    print("> ", end="")
    selection = input()

    if selection == '1':
        for table in TABLES:
            table_info = server2.displayDBSchema(table)
            print(f"\nSchema details for table {table}:")
            print(f"--------------------------------------")
            for column in table_info:
                print(column)

    elif selection == '2':
        data = server2.displayStudentRecords()
        df = pd.DataFrame(data, columns = ['student_id', 'fname', 'lname', 'email', 'mobile', 'course_code', 'units_attempted', 'units_completed', 'course_status'])
        print()
        print(df.to_string(index=False))

    elif selection == '3':
        # INSERT INTO table_name VALUES (value1, value2, value3, ...)
        pass

    elif selection == '4':
        # DELETE FROM table_name WHERE condition
        pass

    elif selection == '5':
        print("Goodbye")
        input()
        exit()

print("Unable to login. Please contact your system administrator.")
input()
exit()