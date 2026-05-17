# # Library Charge Calculation

# days = int(input("Enter the number of days the book was borrowed: "))

# # Calculate charge
# if days <= 5:
#     charge = days * 2
# elif days <= 10:
#     charge = days * 3
# elif days <= 15:
#     charge = days * 4
# else:
#     charge = days * 5

# # Display result
# print("Library Charge = Rs.", charge)



# 13. Library Charge Calculation 
# Problem Statement: 
# Write a javascript program that calculates the library charge based on the number of days a 
# book has been borrowed. 
# Charge Criteria: 
# Instructions: 
# 1. Input: Prompt the user to enter the number of days the book has been borrowed. 
# 2. Processing: Calculate the charge based on the given criteria. 
# 3. Output: Display the calculated charge. 

days = int(input("Enter the Number of Days the Book has been Borrowed : "))

# ● Up to 5 days: Rs. 2 per day 
if days <= 5 and days > -1:
    charge_rs = 2
    total_charge = days * charge_rs
    print(f"The Library Charge is : {total_charge}")

# ● 6 to 10 days: Rs. 3 per day 
elif days >= 6 and days <= 10:
    charge_rs = 3
    total_charge = days * charge_rs
    print(f"The Library Charge is : {total_charge}")

# ● 11 to 15 days: Rs. 4 per day 
elif days >= 11 and days <= 15:
    charge_rs = 4
    total_charge = days * charge_rs
    print(f"The Library Charge is : {total_charge}")

# ● More than 15 days: Rs. 5 per day 
elif days > 15:
    charge_rs = 5
    total_charge = days * charge_rs
    print(f"The Library Charge is : {total_charge}") 