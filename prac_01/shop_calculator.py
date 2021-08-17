"""CP1404 | Prac_01 Shop Calculator | Dannielle Jones"""

DISCOUNT = 0.1

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total = total - (total * DISCOUNT)
print(f"Total price for {number_of_items} items is $ {total:.2f}")
