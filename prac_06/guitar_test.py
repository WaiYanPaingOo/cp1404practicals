from prac_06.guitar import Guitar


def main():
    f_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    s_guitar = Guitar("Another Guitar", 2012, 0)

    print("{} get_age() - Expected 96. Got {}".format(f_guitar.name, f_guitar.get_age()))
    print("{} get_age() - Expected 96. Got {}".format(s_guitar.name, s_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(f_guitar.name, f_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(s_guitar.name, s_guitar.is_vintage()))

    guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while len(name) > 0:
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        temp_guitar = Guitar(name, year, cost)
        guitars.append(temp_guitar)
        name = input("Name: ")

    print("These are my guitars:")

    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""

        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()