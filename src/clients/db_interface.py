import Pyro4
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

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
        data = server2.getDBSchema()

        for key in data:
            print(f"\nSchema for table: {key}")
            print("------------------------------------")
            for line in data.get(key):
                print(line)


    elif selection == '2':
        data = server2.displayStudentRecords()
        headings = ["StudentID", "First Name", "Surname", "Email", "Mobile", "Course Code", "Units Attempted", "Units Completed", "Course Status"]
        df = pd.DataFrame(data, columns=headings)
        with pd.option_context(
            'display.max_rows', None,
            'display.max_columns', None,
        ):
            print(df)


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