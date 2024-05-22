
##THEN RUN THIS FILE SECOND - AFTER RUNNING DB_Controller

import Pyro4
import logging
import time

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Example of existing user_details
# (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')

# Example return of server2.getStudentRecords()
# [('90123456', 'MTH0101', 85, 'HD'), ('90123456', 'MTH0102', 78, 'D')]

@Pyro4.behavior(instance_mode="single")
class Server1(object):
    user_records = []
    user_scores = {}
    numUnitsCompleted = 0
    numOfFails = 0
    course_avg = 0.0
    topEight_avg = 0.0
    person_id = ""
    server2 = None

    # Constructor that makes connection to server-2 when an object is instantiated
    def __init__(self):

        print(f"Attempting to connect to server-2...\n")
        try:
            server_timer_start = time.time()
            # Look up server-2 in the name server
            nameserver = Pyro4.locateNS()
            uri = nameserver.lookup("server-2")

            # Create a Proxy for server-2
            self.server2 = Pyro4.Proxy(uri)

            server_timer_end = time.time()
            print(f"Connected to server-2. Time elapsed {server_timer_end - server_timer_start} seconds\n")
        except:
            print(f"Failed to connect. Timeout after {server_timer_end - server_timer_start} seconds\n")

    @Pyro4.expose
    def validateUser(self, student_id):
        # Attempt to make remote call to server and save the returned value as object attribute
        print("validateUser method called by client.")
        try:
            print("Attempting to retrieve student records from server-2...")
            server_response = self.server2.getStudentRecords(student_id)

            # Firstly, checks if return value is string VALIDATION_ERROR from DB_Controller
            if type(server_response) == str:
                print("Could not retrieve matching student records. Returning authentication error message.")
                return server_response
            else:
                print(f"Student records retrieved from server-2: {server_response[0]}.")
                self.user_records = server_response
                validator_record = self.user_records[0] # (student_id, fname, lname, email, mobile, course_code, units_attempted, units_completed, course_status)
                validator = [validator_record[0], validator_record[1], validator_record[2], validator_record[3]]
                print(f"Returning Validator: {validator} to client.")
                return validator

        except Exception as e:
            logging.exception("Error in validateUser: %s", str(e))

 
    @Pyro4.expose
    def evaluateEligibility(self, user_details):
        print("evaluateEligibility method called by client.")

        self.person_id = user_details[0]

        print("Checking for validated user records...")
        if self.user_records[0][0] == self.person_id:
            print("Validated user records found. Evaluating student records for eligibility.")
            try:
                # Loop through user_records and collect required data
                units = []
                unit_scores = []
                unit_highest_marks = {}

                for record in self.user_records[1:]:
                    unit = record[1]
                    mark = record[2]
                    # Collect number of Fails
                    if record[3] == 'F':
                        self.numOfFails += 1
                    # Collect unique units
                    if unit not in unit_highest_marks:
                        unit_highest_marks[unit] = mark
                    else:
                        if mark > unit_highest_marks[unit]:
                            unit_highest_marks[unit] = mark


                    units = list(unit_highest_marks.keys())
                    unit_scores = list(unit_highest_marks.values())
                    
                    # Calculate averages and store in class attributes
                    self.course_avg = round(sum(unit_scores) / len(unit_scores), 2)
                    unit_scores.sort(reverse = True)
                    self.topEight_avg = round(sum(unit_scores[:8]) / 8, 2)
                    self.numUnitsCompleted = len(units)

            except Exception as e:
                logging.exception("Error in evaluateEligibility: %s", str(e))
        
        # Example of non-student user_details
        # (user_id, {<course_code> : [result1, result2, ...], ...})
        else:
            print("No validated user records found. Evaluating eligibility based on unit scores input by user.")
            try:
                self.person_id = user_details[0]
                self.user_scores = user_details[1]
                self.numUnitsCompleted = len(self.user_scores)

                unit_scores = []
                for key, value in self.user_scores.items():
                    for grade in value:
                        unit_scores.append(grade)
                        if grade < 50:
                            self.numOfFails += 1
                # Calculate averages and store in class attributes
                self.course_avg = round(sum(unit_scores) / len(unit_scores), 2)
                unit_scores.sort(reverse = True)
                self.topEight_avg = round(sum(unit_scores[:8]) / 8, 2)

            except Exception as e:
                logging.exception("Error in evaluateEligibility: %s", str(e))
        
        print("\nReturning eligibility evaluation to client.")
        # Evaluate honours criteria and return string for client
        if self.numUnitsCompleted < 16:
            return f"{self.person_id}, {self.course_avg}, completed less than 16 units!\nDOES NOT QUALIFY FOR HONOURS STUDY!"
        elif self.numOfFails >= 6:
            return f"{self.person_id}, {self.course_avg}, with 6 or more Fails!\nDOES NOT QUALIFY FOR HONOURS STUDY!"
        elif self.course_avg >= 70:
            return f"{self.person_id}, {self.course_avg}, QUALIFIES FOR HONOURS STUDY!"
        elif (self.course_avg < 70 and self.course_avg >= 65) and self.topEight_avg >= 80:
            return f"{self.person_id}, {self.course_avg}, {self.topEight_avg}, QUALIFIES FOR HONOURS STUDY!"
        elif (self.course_avg < 70 and self.course_avg >= 65) and self.topEight_avg < 80:
            return f"{self.person_id}, {self.course_avg}, {self.topEight_avg}, MAY HAVE A GOOD CHANCE! Need further assessment!"
        elif (self.course_avg < 65 and self.course_avg >= 60) and self.topEight_avg > 80:
            return f"{self.person_id}, {self.course_avg}, {self.topEight_avg}, MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator's permission!"
        else:
            return f"{self.person_id}, {self.course_avg}, DOES NOT QUALIFY FOR HONOURS STUDY!"


# Daemon([host=None, port=0, unixsocket=None, nathost=None, natport=None, interface=DaemonObject, connected_socket=None])
host_ip = "192.168.1.111"

def main():
    s1_daemon = Pyro4.Daemon(host=host_ip)
    ns = Pyro4.locateNS(host=host_ip)
    uri = s1_daemon.register(Server1)
    ns.register("server-1", uri)
    s1_daemon.requestLoop()

if __name__ == "__main__":
    main()