# 12.Employee Salary Based on Experience. 
# You are building a system for a Human Resources (HR) department that calculates an 
# employee's salary based on their years of experience. The system assigns salary tiers 
# based on the number of years an employee has been working. It also offers bonuses for 
# employees who have more than 15 years of experience. 
# Scenario Breakdown: 
# Context 1: Senior Employee 
# ● An employee with 10 or more years of experience is classified as a Senior 
# Employee. The base salary for such an employee is 80000. 
# ● If the employee has more than 15 years of experience they receive a bonus of 
# 5000 to their salary. 
# Example: 
# An employee with 18 years of experience: 
# ● They are classified as Senior Employees. 
# ● Their base salary is 80000. 
# ● Since they have more than 15 years of experience they receive an additional 
# 5000 bonus. 
# ● The final salary is 85000. 
# Context 2: Mid-Level Employee 
# ● Employees with 5 to 9 years of experience are classified as Mid-Level 
# Employees. 
# ● Their base salary is 50000 with no bonus. 
# Example: 
# An employee with 7 years of experience: 
# ● They are classified as a Mid-Level Employee. 
# ● Their base salary is 50000. 
# ● Since they have fewer than 10 years of experience no bonus is added. 
# ● The final salary is 50000. 
# Context 3: Junior Employee 
# ● Employees with less than 5 years of experience are classified as Junior 
# Employees. 
# ● Their base salary is 30000 with no bonus. 
# Example: 
# An employee with 3 years of experience: 
# ● They are classified as Junior Employees. 
# ● Their base salary is 30000. 
# ● No bonus is added. 
# ● The final salary is 30000. 
# Output Examples: 
# Senior Employee with 18 years of experience: 
# Enter years of experience: 18 
# Senior employee 
# Experience exceeds 15 years. Bonus added. 
# Salary: 85000 
# Mid-Level Employee with 7 years of experience: 
# Enter years of experience: 7 
# Mid-level employee 
# Salary: 50000 
# Junior Employee with 3 years of experience: 
# Enter years of experience: 3 
# Junior employee 
# Salary: 30000

bonus = 5000
experience = int(input("Enter years of experience : "))

if experience >= 10:

    base_salary = 80000
    print("Senior Employee.")
    print(f"The Base Salary is : {base_salary}")
    print()

    salary = base_salary + bonus
    print("Experience exceeds 15 years. Bonus added.")
    print(f"Salary : {salary}")

elif experience >= 5 and experience <= 9:

    base_salary = 50000
    print("Mid-Level Employee.")
    print(f"The Base Salary is : {base_salary}")
    print("No Bonus is Added.")
    print()
    print(f"Salary : {base_salary}")

elif experience < 5:

    base_salary = 30000
    print("Junior Employee.")
    print(f"The Base Salary is : {base_salary}")
    print("No Bonus is Added.")
    print()
    print(f"Salary : {base_salary}") 