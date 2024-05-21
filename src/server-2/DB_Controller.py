
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
    DB_DIR = "C:\\Users\\krbak\OneDrive\\Uni\\Year 3 Semester 1\\CSI3344 Distributed Systems\\Assignment 3\\Code\\HEPaS\\src\\server-2\\oust_database.db"
    VALIDATION_ERROR = "VALIDATION ERROR: Cannot authenticate user. Student record not found in database."
    TABLE_NAMES = []

    def __init__(self):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        try:
            conn = sqlite3.connect(self.DB_DIR)
        except Exception as e:
            logging.exception("Failed to connect to database: %s", str(e))
            raise
        
        cur = conn.cursor()

        # Collect table names into a list
        for element in cur.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall():
            self.TABLE_NAMES.append(element[0])

        # Close connection to SQL database
        cur.close()


    # Function Purpose: 
    # take a tuple in format (bool, string(student_id), string(fname), string(lname), string(email))
    # and validates details against Student table in database. If it finds a record that
    # matches all elements, queries StudentUnits table and return the below tuple:
        # (student_id, unit_code, unit_score, unit_grade)
        # ('90123456', 'MTH0101', 85, 'HD')
    # Return error message if user cannot be validated.
    @Pyro4.expose
    def getStudentRecords(self, student_id):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        self.cur = conn.cursor()

        # List to collect StudentUnit records and return from function
        student_unit_list = []

        # Validate user against Students table in database
        print("\nComparing fields to rows in oust_database::Table::Students...")
        match_found = False
        while (not match_found):
            for row in self.cur.execute('SELECT student_id FROM Students'):
                if row[0] == student_id:
                    print("\nUser authenticated. Match found in oust_database::Table::Students.")
                    print(row)
                    print("\n")
                    student_unit_list.append(row)
                    match_found = True
            break

        if (not match_found):
            print("ERROR: Cannot authenticate user. Student record not found in oust_database::Table::Students.")
            return self.VALIDATION_ERROR

        # Use the user record to fetch all rows from table StudentUnits corresponding to that user
        query = 'SELECT student_id, unit_code, unit_score, unit_grade FROM StudentUnits WHERE student_id = ?'
        results = self.cur.execute(query, (student_id,)).fetchall()

        for element in results:
            student_unit_list.append(element)

        # Close connection to SQL database
        self.cur.close()

        return student_unit_list

    # ---------------------------------------------
    # FUNCTIONS BELOW ARE CALLED BY db_interface.py
    # ---------------------------------------------

    @Pyro4.expose
    def getDBSchema(self):

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        table_schemas = {}

        # Iterate through table names and collect schema of each table and store in dict
        for table in self.TABLE_NAMES:
            schema_info = cur.execute(f"PRAGMA table_info({table})").fetchall()
            table_columns = []
            
            for column in schema_info:
                    table_columns.append(f"Column: {column[1]}, Type: {column[2]}, Nullable: {column[3]}, Default: {column[4]}")
            
            table_schemas[table] = table_columns

        # Close connection to SQL database
        cur.close()

        return table_schemas


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

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server2: "server-2"
        },
        ns = True
    )

if __name__ == "__main__":
    main()