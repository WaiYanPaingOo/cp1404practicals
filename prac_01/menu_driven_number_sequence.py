number_x = int(input("Enter the first number: "))
number_y = int(input("Enter the second number: "))

while number_x > number_y:
    print("First number must be less than the Second number!")
    number_x = int(input("Enter the first number: "))
    number_y = int(input("Enter the second number: "))
print()

print("A. Show the even numbers from {} to {}".format(number_x, number_y))
print("B. Show the odd numbers from {} to {}".format(number_x, number_y))
print("C. Show the squares from {} to {}".format(number_x, number_y))
print("D. Exit the program")

print()

choice = str(input(">>> ").upper())

while choice != "D":
    if choice == "A":
        print("Even numbers from {} to {} are | ".format(number_x, number_y), end='')
        for i in range(number_x, number_y+1, 1):
            if i % 2 == 0:
                print("{} ".format(i), end='')
        print()
        print()
    elif choice == "B":
        print("Odd numbers from {} to {} are | ".format(number_x, number_y), end='')
        for i in range(number_x, number_y+1, 1):
            if i % 2 != 0:
                print("{} ".format(i), end='')
        print()
        print()
    elif choice == "C":
        print("Squares from {} to {} are | ".format(number_x, number_y), end='')
        for i in range(1, number_y+1//2, 1):
            if i * i <= number_y:
                square_number = i * i
                print("{} ".format(square_number), end='')
        print()
        print()
    else:
        print("Invalid Choice!")
    print("A. Show the even numbers from {} to {}".format(number_x, number_y))
    print("B. Show the odd numbers from {} to {}".format(number_x, number_y))
    print("C. Show the squares from {} to {}".format(number_x, number_y))
    print("D. Exit the program")

    choice = str(input(">>> ").upper())

print("Application Exited, Thank You!")
