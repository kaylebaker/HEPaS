
##OPEN COMMAND LINE, TYPE "pyro4-ns" FIRST

##THEN RUN THIS FILE ---> THEN RUN RMI_Controller

import sqlite3
import Pyro4
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@Pyro4.behavior(instance_mode="single")
class Server2(object):
    # Set constants
    DB_DIR = ".\oust_database.db"
    VALIDATION_ERROR = "ERROR: Cannot authenticate user. Student record not found in database."


    # Function Purpose: 
    # take a tuple in format (bool, string(student_id), string(fname), string(lname), string(email))
    # and validates details against Student table in database. If it finds a record that
    # matches all elements, queries StudentUnits table and return the below tuple:
        # (student_id, unit_code, unit_score, unit_grade)
        # ('90123456', 'MTH0101', 85, 'HD')
    # Return error message if user cannot be validated.
    @Pyro4.expose
    def getStudentRecords(self, user_details):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        # List to collect StudentUnit records and return from function
        student_unit_list = []

        # Check boolean value at user_details[0] to confirm if current/former student
        # Example of user_details
        # (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')
        if user_details[0] == True:
            print("First element of input tuple is 'True'. Validating user in oust_database::Table::Students.")
            
            # Create tuple to compare to SQL query rows
            validator = (user_details[1], user_details[2], user_details[3], user_details[4])

        # Validate user against Students table in database
        print("\nComparing fields to rows in oust_database::Table::Students...")
        match_found = False
        while (not match_found):
            for row in cur.execute('SELECT student_id, fname, lname, email FROM Students'):
                if row == validator:
                    print("\nUser authenticated. Match found in oust_database::Table::Students.")
                    print(row)
                    print("\n")
                    match_found = True
            break

        if (not match_found):
            print("ERROR: Cannot authenticate user. Student record not found in oust_database::Table::Students.")
            return self.VALIDATION_ERROR

        # Use the user record to fetch all rows from table StudentUnits corresponding to that user
        query = 'SELECT student_id, unit_code, unit_score, unit_grade FROM StudentUnits WHERE student_id = ?'
        results = self.cur.execute(query, (user_details[1],)).fetchall()

        for element in results:
            student_unit_list.append(element)

        # Close connection to SQL database
        cur.close()

        return student_unit_list


    # ---------------------------------------------
    # FUNCTIONS BELOW ARE CALLED BY db_interface.py
    # ---------------------------------------------

    @Pyro4.expose
    def displayDBSchema(self, table_name):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        table_info = []
        schema_info = cur.execute(f"PRAGMA table_info({table_name})").fetchall()
        for column in schema_info:
            table_info.append(f"Column: {column[1]}, Type: {column[2]}, Nullable: {column[3]}, Default: {column[4]}")

        # Close connection to SQL database
        cur.close()

        return table_info


    @Pyro4.expose
    def displayStudentRecords(self):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        data = []
        for record in cur.execute('SELECT * FROM Students'):
            row_data = [record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8]]
            data.append(row_data)

        # Close connection to SQL database
        cur.close()

        return data


    @Pyro4.expose
    def addRecord(self, table_name, record):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        try:

            cur.execute(f'INSERT INTO {table_name} {record}')
            if cur.rowcount == 1:
                print("Record added successfully.")
            else:
                print("No record was inserted.")

            # Close connection to SQL database
            cur.close()

        except Exception as e:
            print("ERROR: Unable to insert new record.", e)

            # Close connection to SQL database
            cur.close()


    @Pyro4.expose
    def deleteRecord(self, table_name, identifier):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

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

            # Close connection to SQL database
            cur.close()

        except Exception as e:
            print("ERROR: Unable to delete record.", e)

            # Close connection to SQL database
            cur.close()



def main():
    Pyro4.Daemon.serveSimple(
        {
            Server2: "server-2"
        },
        ns = True
    )

if __name__ == "__main__":
    main()