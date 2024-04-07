# Students that have more than 15 Student unit records
# ('89140352', 'John', 'Doe', 'john.doe@gmail.com', '0412345678', 'B65', 4, 4, 'Active'),
# ('20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com', '0423456789', 'M75', 3, 2, 'Inactive')

import Pyro4
import sqlite3

# Look up server-1 in the name server
nameserver = Pyro4.locateNS()
uri = nameserver.lookup("server-1")

# Create a Proxy for server-2
server1 = Pyro4.Proxy(uri)

user_details1 = (True, '89140352', 'John', 'Doe', 'john.doe@gmail.com')
user_details2 = (True, '20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com')

print(server1.evaluateEligibility(user_details1))
print(server1.evaluateEligibility(user_details2))