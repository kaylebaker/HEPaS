import Pyro4

# Example of user_details
# (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')

# Example return of server2.getStudentRecords()
# [(18, '90123456', 'MTH0101', 'Calculus I', 85, 'HD', 2021, 1, None), (19, '90123456', 'MTH0102', 'Calculus II', 78, 'D', 2021, 2, None)]

@Pyro4.behavior(instance_mode="percall")
class Server1(object):
    user_details = []
    user_records = []
    numUnitsCompleted = 0
    numOfFails = 0
    auth_error = ""

    # Constructor that makes connection to server-2 when an object is instantiated
    def __init__(self):
        # Look up server-2 in the name server
        nameserver = Pyro4.locateNS()
        uri = nameserver.lookup("server-2")

        # Create a Proxy for server-2
        self.server2 = Pyro4.Proxy(uri)

    @Pyro4.oneway
    def storeUserDetails(self, user_details):
        self.user_details = user_details
        # Attempt to make remote call to server and save the returned value
        try:
            server_response = self.server2.getStudentRecords(user_details)
            if type(server_response) == str:
                self.auth_error = server_response
            else:
                self.user_records = server_response

                # Calculate number of unique units in records
                units = []
                for record in self.user_records:
                    if record[2] not in units:
                        units.append(record[2])
                    if record[5] == 'F':
                        self.numOfFails += 1
                self.numUnitsCompleted = len(units)

        except:
            print("Could not contact server.")
            return 0


    def calculateCourseAverage(self):
        unit_scores = []

        for record in self.user_records:
            unit_scores.append(record[4])

        average = sum(unit_scores) / len(unit_scores)

        return round(average, 2)
    

    def calculateBestEightAverage(self):
        unit_scores = []

        for record in self.user_records:
            unit_scores.append(record[4])

        # Sort list in descending order
        unit_scores.sort(reverse = True)
        
        average = sum(unit_scores[:8]) / 8

        return round(average, 2)
        
    
    @Pyro4.expose
    def evaluateEligibility(self):

        # Store student_id and course average as variables
        person_id = self.user_details[2]
        course_avg = self.calculateCourseAverage()
        topEight_avg = self.calculateBestEightAverage()

        if self.numUnitsCompleted < 16:
            return f"{person_id}, {course_avg}, completed less than 16 units!\nDOES NOT QUALIFY FOR HONOURS STUDY!"
        elif self.numOfFails >= 6:
            return f"{person_id}, {course_avg}, with 6 or more Fails!\nDOES NOT QUALIFY FOR HONOURS STUDY!"
        elif course_avg >= 70:
            return f"{person_id}, {course_avg}, QUALIFIES FOR HONOURS STUDY!"
        elif (course_avg < 70 and course_avg >= 65) and topEight_avg >= 80:
            return f"{person_id}, {course_avg}, {topEight_avg}, QUALIFIES FOR HONOURS STUDY!"
        elif (course_avg < 70 and course_avg >= 65) and topEight_avg < 80:
            return f"{person_id}, {course_avg}, {topEight_avg}, MAY HAVE A GOOD CHANCE! Need further assessment!"
        elif (course_avg < 65 and course_avg >= 60) and topEight_avg > 80:
            return f"{person_id}, {course_avg}, {topEight_avg}, MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator's permission!"
        else:
            return f"{person_id}, {course_avg}, DOES NOT QUALIFY FOR HONOURS STUDY!"
        

def main():
    Pyro4.Daemon.serveSimple(
        {
            Server1: "server-2"
        },
        ns = True
    )

if __name__ == "__main__":
    main()