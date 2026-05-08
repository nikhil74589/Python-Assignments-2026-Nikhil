# Apply a 20% discount to a price
price = 1000
discount_percentage = 20
print(f"Aefore discount the price is : {price}")
print(f"Discount is given by : {discount_percentage}")

discount = (price *discount_percentage) / 100
discounted_price = price - discount

print(f"After discount the price is : {discounted_price}")