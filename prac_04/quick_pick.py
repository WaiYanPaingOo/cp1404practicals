import random

PICKS = []


def main():
    number_of_picks = int(input("Enter how many quick picks: "))
    temp_list = []

    for outer_loop in range(0, number_of_picks, 1):
        temp_list.clear()
        first_num = random.randint(1, 44)
        print("{0:>3}".format(first_num), end='  ')
        temp_list.append(first_num)
        for inner_loop in range(0, 4, 1):
            next_num = random.randint(1, 44)
            while next_num in temp_list:
                next_num = random.randint(1, 44)
            print("{0:>3}".format(next_num), end='  ')
            temp_list.append(next_num)
        print(" ")
        PICKS.append(temp_list)


main()
