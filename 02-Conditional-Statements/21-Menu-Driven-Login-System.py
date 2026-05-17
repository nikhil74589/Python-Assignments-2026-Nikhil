# All  ready defined credentials :
phone_number = "1234567890"
otp = "1234"

email = "nikhilranjan435@gmail.com"
password = "password123"

# Display menu :
print("===== Login System =====")
print("1. Login with Phone")
print("2. Login with Email")
print("3. Exit")

# User choice :
choice = input("Enter your choice (1/2/3): ")

# Option 1 - Phone Login :
if choice == "1":
    user_phone = input("Enter phone number: ")
    user_otp = input("Enter OTP: ")

    if user_phone == phone_number and user_otp == otp:
        print("Login successful with phone!")
    else:
        print("Invalid phone number or OTP!")

# Option 2 - Email Login :
elif choice == "2":
    user_email = input("Enter email: ")
    user_password = input("Enter password: ")

    if user_email == email and user_password == password:
        print("Login successful with email!")
    else:
        print("Invalid email or password!")

# Option 3 - Exit :
elif choice == "3":
    print("Exiting the program. Have a nice day!")

# Invalid choice :
else:
    print("Invalid choice! Please select a valid option.")