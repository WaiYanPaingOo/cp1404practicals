from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "Let's drive!\nq)uit, c)hoose taxi, d)rive"


def main():
    """Main"""
    print(MENU)
    # user_input = str(input(">>> "))
    user_input = input_checker(">>> ")

    while user_input.upper() != 'Q':
        # TODO
        user_input = input_checker(">>> ")


def input_checker(txt):
    is_accepted = False
    while not is_accepted:
        user_input = str(input(txt))
        if len(user_input) == 0:
            print("Please make a selection")
        else:
            return user_input


main()