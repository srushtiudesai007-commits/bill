n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    price = float(input("Enter item price: "))
    total = total + price

print("Total Bill =", total)