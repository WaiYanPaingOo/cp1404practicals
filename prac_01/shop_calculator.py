number_of_item = int(input("Enter Number of items: "))
temp_amount = 0.0
result = 0.0

for i in range(0, number_of_item, 1):
    item_price = float(input("Enter Price of item:$ "))
    temp_amount += item_price

if temp_amount > 100:
    result = temp_amount-(temp_amount * (10/100))
else:
    result = temp_amount
print("Total Price for {} items is ${:.2f}".format(number_of_item, result))
