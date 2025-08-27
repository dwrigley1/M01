'''
One part of the CIA triad that is shown here is Confidentiality.
When the admin credentials are entered, the adminRole() function is triggered.
When the user credentials are entered, the userRole() function is triggered.
When incorrect credentials are entered, the loginFailure() function is triggered.
'''

admin_username = "admin"
admin_password = "apw"
user_username = "user"
user_password = "upw"

def adminRole():
    print("Admin page is loaded, all features are available.")

def userRole():
    print("User page is loaded, restricted to what the admin user allows this person to see.")

def loginFailure():
    print("Hmm. Something went wrong, please try again.")

username = input("Enter Your Username: ")
password = input("Enter Your Password: ")
if username == admin_username and password == admin_password:
    adminRole()
elif username == user_username and password == user_password:
    userRole()
else:
    loginFailure()