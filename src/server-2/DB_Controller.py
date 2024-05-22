
##OPEN COMMAND LINE, TYPE "pyro4-ns" FIRST

##THEN RUN THIS FILE ---> THEN RUN RMI_Controller

import sqlite3
import Pyro4
import logging
import time
import pathlib

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@Pyro4.behavior(instance_mode="single")
class Server2(object):
    # Set constants
    #DB_DIR = "C:\\Users\\krbak\OneDrive\\Uni\\Year 3 Semester 1\\CSI3344 Distributed Systems\\Assignment 3\\Code\\HEPaS\\src\\server-2\\oust_database.db"
    DB_DIR = str(pathlib.Path(__file__).parent.resolve()) + "\\oust_database.db"
    VALIDATION_ERROR = "VALIDATION ERROR: Cannot authenticate user. Student record not found in database."

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
        print("getStudentRecords method called by server-1.")
        server_timer_start = time.time()
        print(f"Attempting to connect to SQLite database...\n")

        conn = sqlite3.connect(self.DB_DIR)
        self.cur = conn.cursor()

        server_timer_end = time.time()
        print(f"Connected to database. Time elapsed {server_timer_end - server_timer_start} seconds\n")

        # List to collect StudentUnit records and return from function
        student_unit_list = []

        # Validate and collect student records based on student id
        print("\nComparing fields to rows in oust_database::Table::Students...")
        match_found = False
        while (not match_found):
            for row in self.cur.execute('SELECT student_id, fname, lname, email FROM Students'):
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

        print("Collecting student records from oust_database::Table::StudentUnits.")
        for element in results:
            student_unit_list.append(element)

        # Close connection to SQL database
        self.cur.close()
        print("Connection to database closed.")
        print("Returning list of StudentUnit records to server-1")

        return student_unit_list

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server2: "server-2"
        },
        ns = True
    )

if __name__ == "__main__":
    main()