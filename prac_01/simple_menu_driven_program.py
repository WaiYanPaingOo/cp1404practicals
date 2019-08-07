
menu = """(H)ello
(G)oodbye
(Q)uit"""

user_name = str(input("Enter name: "))
print(menu)

option = str(input(">>> "))

while option != 'Q':
    if option == 'H':
        print("Hello {}".format(user_name))
    elif option == 'G':
        print("Goodbye {}".format(user_name))
    else:
        print("Invalid choice!")
    print(menu)
    option = str(input(">>> "))

print("Finished.")
