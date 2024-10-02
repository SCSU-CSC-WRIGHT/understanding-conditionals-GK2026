## Password Checker
#Set an admin password. Ask the user to input a password. If the entered password matches the admin password, print "Access granted." If not, print "Access denied."
admin=("GraceKirby13")#Set admin password
password=input("Enter a password: ")#Gets password from user
if(password==admin):#checks password aginst admin
    print("Access granted")#If they are equal than prints access granted
else:
    print("Access denied")#The password is wrong