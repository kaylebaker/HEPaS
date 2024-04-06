import Pyro4

# Look up server-1 in the name server
nameserver = Pyro4.locateNS()
uri = nameserver.lookup("server-1")

# Create a Proxy for server-2
server1 = Pyro4.Proxy(uri)

user_details = (True, '90123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')
user_details2 = (True, '10123456', 'Matthew', 'Rodriguez', 'matthew.rodriguez@example.com')

print(server1.evaluateEligibility(user_details))