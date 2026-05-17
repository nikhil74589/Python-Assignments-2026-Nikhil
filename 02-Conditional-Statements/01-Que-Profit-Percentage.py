# Calculate Profit Percentage :

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

print("-"*40)

if selling_price > cost_price :

    profit = selling_price - cost_price
    profit_percentage = ((selling_price - cost_price) / cost_price)* 100
    print(f"Result: Profit")
    print(f"profit of the percentage is : {profit_percentage}%")

elif cost_price > selling_price :

     loss = cost_price - selling_price
     loss_percentage = ((cost_price - selling_price) /cost_price) *100
     print(f"Result: loss ")
     print(f"loss of the perecentage is : {loss_percentage}%")

else:
    print("No profit, no loss (Break-even).")     

