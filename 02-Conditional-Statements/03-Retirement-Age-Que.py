# Retirement Age Calculator 

retirement_age = 65

age = int(input("please enter your current age : "))

if age >= retirement_age :
     print ("Congratulations ! You have already reached at the retirement age ")
else :
      years_left = (retirement_age - age )
print(f"You have {years_left} years left until you reach retirement age : ") 

