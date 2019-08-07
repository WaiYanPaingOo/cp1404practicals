for i in range(1, 21, 2):
    print(i, end=' ')
print()
print("___________________________________")

for i in range(0, 101, 10):
    print(i, end=' ')
print()
print("___________________________________")

for i in range(20, 0, -1):
    print(i, end=' ')
print()
print("___________________________________")

count = int(input("Enter count: "))
for i in range(0, count, 1):
    print("*", end=' ')
print()
print("___________________________________")

count = int(input("Enter count: "))
for outer_loop in range(1, count+1, 1):
    for inner_loop in range(0, outer_loop, 1):
        print("*", end=' ')
    print()
print()
print("___________________________________")

MENU = """Negative Number - Quit"""
print(MENU)
sales = float(input("Enter sales: $"))
bonus = 0;
while sales >= 0:
    if sales < 1000:
        bonus = sales * (10/100)
    else:
        bonus = sales * (15/100)
    print("Bonus: $ {} ".format(bonus))
    print()
    print(MENU)
    sales = float(input("Enter sales: $"))
print("Thank you.")
print()
print("___________________________________")


