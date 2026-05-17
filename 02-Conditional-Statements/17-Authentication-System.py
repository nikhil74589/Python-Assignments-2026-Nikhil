# All ready defined credentials :
valid_username = "Nikhil Ranjan"
valid_password = "pass@123"

# Taking input from user :
username = input("Enter username: ")
password = input("Enter password: ")

# Checking credentials :
if username == valid_username and password == valid_password:
    print("Authentication successful.")
else:
    print("Authentication failed.")