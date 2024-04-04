import sqlite3

class OUSTDatabase:
    def __init__(self, user_details):
        self.user_details = user_details
        self.DB_DIR = "src\server-2\database\oust_database.db"
        self.VALIDATION_ERROR = "ERROR: Cannot authenticate user. Student record not found in database."

    # Function Purpose: take a tuple in format (bool, string(student_id), string(fname), string(lname), string(email))
    #                   and validates details against Student table in database. If it finds a record that
    #                   matches all elements, queries StudentUnits table and return all rows that correspond
    #                   to the student_id as a list. Return error message if user cannot be validated.
    def getStudentRecords(self):

        # Variable to hold the user record (if found)
        user_record = ()

        # List to collect StudentUnit records and return from function
        student_unit_list = []

        # Establish connection to SQLite database and create cursor object to perform SQL operations
        conn = sqlite3.connect(self.DB_DIR)
        cur = conn.cursor()

        # Check boolean value at user_details[0] to confirm if current/former student
        # Assign each element of the tuple to variables
        if self.user_details[0] == True:
            print("First element of input tuple is 'True'. Validating user in oust_database::Table::Students.")
            # Variables for validating user
            student_id = str(self.user_details[1])
            print("student_id = " + student_id)
            fname = self.user_details[2]
            print("fname = " + fname)
            lname = self.user_details[3]
            print("lname = " + lname)
            email = self.user_details[4]
            print("email = " + email)
        
        # Validate user against Students table in database
        print("\nComparing fields to rows in oust_database::Table::Students...")
        match_found = False
        while (not match_found):
            for row in cur.execute('SELECT * FROM Students'):
                if row[0] == student_id and row[1] == fname and row[2] == lname and row[3] == email:
                    print("\nUser authenticated. Match found in oust_database::Table::Students.")
                    print(row)
                    print("\n")
                    match_found = True

        if (not match_found):
            print("ERROR: Cannot authenticate user. Student record not found in oust_database::Table::Students.")
            return self.VALIDATION_ERROR
        
        # Use the user record to fetch all rows from table StudentUnits corresponding to that user
        query = 'SELECT * FROM StudentUnits WHERE student_id = ?'
        results = cur.execute(query, (student_id,)).fetchall()

        # Close the connection
        conn.close()

        for element in results:
            student_unit_list.append(element)

        return student_unit_list


def main():
    test_tuple = (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')
    oustRMI = OUSTDatabase(test_tuple)
    RMI_results = oustRMI.getStudentRecords()
    print(RMI_results)

if __name__ == "__main__":
    main()