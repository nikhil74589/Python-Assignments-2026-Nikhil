# Validating Email Domain in Python :

# Email input from user
email = input("Enter your email address: ")

# Checking if email have gmail.com.

if "gmail.com" in email:
    print("Email is eligible for registration.")
else:
    print("Email is not eligible for registration.")