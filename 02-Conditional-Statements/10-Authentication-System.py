# Authentication System in Python:

# Predefined credantials.

valid_username = "Nikhil"
valid_password = "pass@123"

# Taking input from system.

username = input("Enter username: ")
password = input("Enter password: ")

# Checking username and password

if username == valid_username and password == valid_password:
    print("Login Successful!")
else:
    print("Invalid Username or Password")