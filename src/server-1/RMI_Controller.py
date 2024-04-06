
##THEN RUN THIS FILE SECOND - AFTER RUNNING DB_Controller

import Pyro4
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Example of user_details
# (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')

# Example return of server2.getStudentRecords()
# [('90123456', 'MTH0101', 85, 'HD'), ('90123456', 'MTH0102', 78, 'D')]

@Pyro4.behavior(instance_mode="single")
class Server1(object):
    user_details = ()
    user_records = []
    numUnitsCompleted = 0
    numOfFails = 0
    course_avg = 0.0
    topEight_avg = 0.0
    person_id = ""
    server2 = None

    # Constructor that makes connection to server-2 when an object is instantiated
    def __init__(self):
        # Look up server-2 in the name server
        nameserver = Pyro4.locateNS()
        uri = nameserver.lookup("server-2")

        # Create a Proxy for server-2
        self.server2 = Pyro4.Proxy(uri)

 
    @Pyro4.expose
    def evaluateEligibility(self, user_details):
        # Store user details as object attribute
        self.user_details = user_details
        self.person_id = self.user_details[2]

        # Attempt to make remote call to server and save the returned value as object attribute
        try:
            server_response = self.server2.getStudentRecords(user_details)
            if type(server_response) == str:
                return server_response
            else:
                self.user_records = server_response

                # Loop through user_records and collect required data
                units = []
                unit_scores = []

                for record in self.user_records:
                    # Collect unique units
                    if record[1] not in units:
                        units.append(record[1])

                    # Collect number of Fails
                    if record[3] == 'F':
                        self.numOfFails += 1

                    # Collect unit scores to calculate averages
                    unit_scores.append(record[2])

                self.course_avg = sum(unit_scores) / len(unit_scores)
                unit_scores.sort(reverse = True)
                self.topEight_avg = sum(unit_scores[:8]) / 8
                self.numUnitsCompleted = len(units)

        except Exception as e:
            logging.exception("Error in evaluateEligibility: %s", str(e))


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
        

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server1: "server-1"
        },
        ns = True
    )

if __name__ == "__main__":
    main()