# Input number of days :

days = int(input("Enter number of days book was borrowed: "))

# Calculate charges :

if days <= 5:
    charge = days * 2
elif days <= 10:
    charge = days * 3
elif days <= 15:
    charge = days * 4
else:
    charge = days * 5

# Display total charges :

print("Total Library Charges = ₹", charge)