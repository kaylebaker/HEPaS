# Students that have more than 15 Student unit records
# ('89140352', 'John', 'Doe', 'john.doe@gmail.com', '0412345678', 'B65', 4, 4, 'Active'),
# ('20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com', '0423456789', 'M75', 3, 2, 'Inactive')

import Pyro4
import time

print("Connecting to server-1...")
server_timer_start = time.time()

# Look up server-1 in the name server
nameserver = Pyro4.locateNS()
uri = nameserver.lookup("server-1")

# Create a Proxy for server-2
server1 = Pyro4.Proxy(uri)

server_timer_end = time.time()
print(f"Connected to server-1. Time elapsed {server_timer_end - server_timer_start} seconds\n")

print("")

print("This is a test client. The following user records will be used to test the system:")
print("(True, '89140352', 'John', 'Doe', 'john.doe@gmail.com')")
print("(True, '20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com')")
print("(True, '20385631', 'Jane', 'Smith', 'jane.smith@yahoo.com')" + "<== INVALID STUDENT_ID\n")


user_details1 = (True, '89140352', 'John', 'Doe', 'john.doe@gmail.com')
user_details2 = (True, '20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com')
user_details3 = (True, '20385631', 'Jane', 'Smith', 'jane.smith@yahoo.com')


start_time1 = time.time()
print("Executing first call to server-1...")
print(server1.evaluateEligibility(user_details1))
end_time1 = time.time()
print(f"Elapsed time for first call -> {end_time1 - start_time1} seconds\n")

start_time2 = time.time()
print("Executing second call to server-1...")
print(server1.evaluateEligibility(user_details2))
end_time2 = time.time()
print(f"Elapsed time for second call -> {end_time2 - start_time2} seconds\n")

start_time3 = time.time()
print("Executing third call to server-1...")
print(server1.evaluateEligibility(user_details3))
end_time3 = time.time()
print(f"Elapsed time for third call -> {end_time3 - start_time3} seconds\n")

(print("Press Enter to exit..."))
input()