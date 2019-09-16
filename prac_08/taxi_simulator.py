from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main"""
    print("Let's Drive!")
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = ""
    bill_to_date = 0
    user_input = input_checker(">>> ")

    while user_input.upper() != 'Q':
        if user_input.upper() == 'C':
            show_taxi(taxis)
            taxi_num = int_input_checker("Choose taxi: ")

            if taxi_num <= len(taxis):
                current_taxi = taxis[taxi_num-1]
                print("Bill to date: ${}".format(bill_to_date))
            else:
                print("Taxi doesn't exist in No.{}".format(taxi_num))

        elif user_input.upper() == 'D':
            # TODO
            print("drive")
        else:
            print("Invalid input! Please Make a Selection")

        print(MENU)
        user_input = input_checker(">>> ")


def int_input_checker(txt):
    is_accepted = False
    while not is_accepted:
        user_input = input_checker(txt)
        if user_input.isdigit():
            if int(user_input) > 0:
                return int(user_input)
            else:
                print("Enter a digit number greater than 0")
        else:
            print("Enter a digit number")


def input_checker(txt):
    is_accepted = False
    while not is_accepted:
        user_input = str(input(txt))
        if len(user_input) == 0:
            print("Please make a selection")
        else:
            return user_input


def show_taxi(data):
    print("Taxis available:")
    count = 1
    for taxi in data:
        print("{0} - {1}".format(count, taxi))
        count += 1




main()