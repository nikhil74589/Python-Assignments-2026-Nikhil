# Bank Loan Approval System .

print("we are going to check you are eligible or not eligible for loan")
print("For eligibilty we are going to check some points which are as follows" "\n.age criteria",
      "\n2.monthly income"
      "\n3.credit score"
      "\n4.outstanding debts")
age=int(input("please enter your age = "))
monthly_income=int(input("please enter your monthly income = "))
credit_score=int(input("please enter your credit score = "))
outstanding_debt=int(input("please enter your outstanding debt = "))
if age>=18 and age<=60 and monthly_income>=25000 and age>=18 and age<=60 and outstanding_debt<=10000 :
    print("You are eligible for loan")
else :
    print("loan is rejected")    
