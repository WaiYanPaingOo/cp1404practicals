def main():
    """WaiYanPaingOo"""
    FREQUENCY = 3
    name_count, user_name = get_name()

    print_name(name_count, user_name, FREQUENCY)


def print_name(name_count, user_name, freq):
    print("Your Name is: ", end='')
    for i in range(0, name_count, freq):
        print(user_name[i], end='')


def get_name():
    user_name = input("Enter your name: ")
    name_count = len(user_name)
    while name_count == 0:
        print("User name cannot be empty!")
        user_name = input("Enter your name: ")
        name_count = len(user_name)
    return name_count, user_name


main()
