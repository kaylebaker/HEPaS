# Students that have more than 15 Student unit records
# ('89140352', 'John', 'Doe', 'john.doe@gmail.com', '0412345678', 'B65', 4, 4, 'Active'),
# ('20785631', 'Jane', 'Smith', 'jane.smith@yahoo.com', '0423456789', 'M75', 3, 2, 'Inactive')


#clean up docs/ cli
#how to set IP addresses/ set up on different/ multiple pcs
#--------- possible automate script?
#logs for backend
#make cli look good


import Pyro4
import time
import re

def student():
    ud = []
    
    while True:
        SID = (str(input("please enter student number: ")))
        if(SID == "stop"):
            input("Thanks for trying!")
            exit()
        elif (len(SID) != 8):
            print("That is not a valid student number. \nTry again.")
        else:
            ud.append(SID)
            print("\n(Student Number: " + SID + ")\n")
            # Async call to server-1 to return user records based on student id
            validation_result = server1.validateUser(SID)
            break


    alpha_name = True
    while True:
        name = str(input("Please enter name: "))
        
        for i in range(len(name.split())):
            if ( not name.split()[i].isalpha()):
                print("\nInteresting name. Please only enter letters.\n")
                alpha_name = False
            elif (len(name.split()) ==1):
                print("\nEnter all your names please.\n")
                alpha_name = False
            else:
                alpha_name = True
                continue
                
        if alpha_name == True:
            fname = name.split()[0]
            lname = name.split()[-1]
            mname = ''.join([(x[0].capitalize()+". ") for x in name.split()]) 
            print("\n(Name: "+fname.capitalize() + mname[2:-3] + lname.capitalize()+")\n")
            ud.append(fname.capitalize())
            ud.append(lname.capitalize())
            break
    
    while True:
        email = str(input("Please enter email: "))
        if (email.count("@") != 1 or email.count(".com") != 1):           ##be more specific to prevent "@nope" as an email
            print("\nInvalid email address.\n")
        elif( email.find("@") > email.find(".com")):
              print("\nInvalid email address.\n")
        else:
            print("\n(Email: " + email+")\n")
            ud.append(email)
            break

    # Validate user details against return results from async call
    if validation_result.value == ud:
        print(f"Student ID {ud[0]} authenticated!")
        print(f"Calculating eligibility for {ud[1]} {ud[2]}...\n")
        return(ud)
    else:
        print(validation_result.value)
        return False

# Example of non-student user_details
# (user_id, {<course_code> : [result1, result2, ...], ...})

def guest():
    gd = []
    SID = (str(input("Please enter a personal identifier: \n")))
    guest_mark = {}
    mark_quantity = 0
    valid_entry = True
    while valid_entry:      
        unit_code_mark = str(input("\nPlease enter the unit code and mark, seperated by a space. ('wut1337 82') \nType 'stop' when finished. \n\n")) #3letter 4 number
        
        if (unit_code_mark == "stop" or mark_quantity ==30):
            if mark_quantity <16:
                print("insufficient number of units.\nPlease enter more.")
                continue
            if mark_quantity ==30:
                print("Maximum number of entries reached.")
            gd.append(SID)
            gd.append(guest_mark)
            print("\nCalculating eligibility for",gd[1],"...\n")
            return(gd)
            break
        if (len(unit_code_mark.split()) == 2):
            try:
                unit_code = str((unit_code_mark.split())[0])
                unit_mark = float((unit_code_mark.split())[1])
            except ValueError:
                print("\nInvalid format.\n")
                continue
            if (re.match(r"^[A-Za-z]{3,4}\d{3,5}$", unit_code) and 0 <= float(unit_mark) and float(unit_mark) <= 100 ):
                print(f"\n-----------------------------------------------\n{SID}'s marks:")
                if unit_code not in guest_mark:
                    guest_mark[unit_code] = [unit_mark]
                    mark_quantity +=1
                else:
                    guest_mark[unit_code].append(unit_mark)
                    mark_quantity +=1
                for x in guest_mark:
                    if len(guest_mark[x])>1:
                        print(x, end=" : ")
                        for i, y in enumerate(guest_mark[x]):
                            if i < len(guest_mark[x]) - 1:
                                print(y, end=", ")
                            else:
                                print(y)
                    else:
                        for y in guest_mark[x]:
                            print(x,":",y)
                if mark_quantity <= 16:
                    print(f"{16-mark_quantity} more results required.")
                elif mark_quantity >=16 and mark_quantity <=30:
                    print(f"{30-mark_quantity} more results permitted.")
                print("-----------------------------------------------")
                for x in guest_mark:
                    if len(guest_mark[x])>3:
                        print("\n\nSorry, you cannot do a unit more than 3 times.\n\n")
                        valid_entry = False
                        break
                    elif len(guest_mark[x])>1:
                        for i, y in enumerate(guest_mark[x]):
                            if i >= 2 and float(y) < 50:
                                print("\n\nI'm sorry, you are not eligible for honours due to failing a unit more than twice.\n\n")
                                valid_entry = False
                                break

                            
            else:
                print("\nInvalid format.\n")

server_timer_start = time.time()
# # Look up server-1 in the name server
nameserver = Pyro4.locateNS(host="192.168.1.111")
uri = nameserver.lookup("server-1")

# # Create a Proxy for server-2
server1 = Pyro4.Proxy(uri)
server1._pyroAsync()

server_timer_end = time.time()
print(f"Connected to server-1. Time elapsed {server_timer_end - server_timer_start} seconds\n")

current_user = []
while True:
    firstQuestion = input("Are you a former/current student interested in enrolling in an honors course?\n(y/n)\n\n")
    if (firstQuestion.lower() == "y" or firstQuestion.lower() == "yes"):
        print("Welcome, Student!")
        current_user = student()
        print(server1.evaluateEligibility(current_user).value if current_user is not False else "Please try again with valid user credentials.")
        break
    elif(firstQuestion.lower() == "n" or firstQuestion.lower() == "no"):
        print("Welcome, Guest!")
        current_user = guest()
        break
    else:
        print("Please answer yes or no.")



# user_details1 = current_user  #E.g. ('8914352', 'John', 'Doe', 'john.doe@gmail.com')

# #start_time1 = time.time()
# print(server1.evaluateEligibility(user_details1))
# #end_time1 = time.time()
# #print(f"Elapsed time for first call -> {end_time1 - start_time1} seconds\n")

# (print("\nPress Enter to exit..."))
# input()
