# Calculate compound interest :

Principal = 10000

Rate = 5

Time = 2

print(f"The Principal amount is : {Principal}")
print(f"The Rate is : {Rate}")
print(f"The Time is : {Time}")

print("-"*40)

total_amount = Principal * (1 + Rate/100)**2
compound_interest = total_amount - Principal

print (f"The compound interest is : {compound_interest}")
