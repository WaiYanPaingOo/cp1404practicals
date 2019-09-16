from prac_08.unreliable_car import UnReliableCar


def main():
    car1 = UnReliableCar("Prius 1", 100, 55.8)
    car1.drive(40)
    print(car1)


main()