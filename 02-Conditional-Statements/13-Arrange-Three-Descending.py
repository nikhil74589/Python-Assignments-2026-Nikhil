# Input three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Sorting in descending order
numbers = [num1, num2, num3]
numbers.sort(reverse=True)

# Output
print("Numbers in Descending Order:", numbers[0], numbers[1], numbers[2])