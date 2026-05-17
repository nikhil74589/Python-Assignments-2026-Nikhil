# Salary Calculation .

Base_Salary = 50000 
Bonus = 5000  
Tax_Rate = 0.10   
Other_Charges = 2000 

# 1 Calculate gross salary (Base + Bonus )
Gross_salary = Base_Salary + Bonus

# 2 Calculate Tax ( 10 % of gross salary )
Tax_amount = Gross_salary * Tax_Rate

# 3 Calculate Net salary (Gross - Tax - Other charges)
Net_salary = Gross_salary - Tax_amount - Other_Charges

print(f"Gross salary : {Gross_salary} ")
print(f"Tax (10%) : {Tax_amount} ")
print(f"Net Salary : {Net_salary}")
