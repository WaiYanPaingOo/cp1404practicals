from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi1 = SilverServiceTaxi("Hummer", 200, 2)
    print(silver_taxi1)
    silver_taxi1.drive(18)
    print(silver_taxi1)
    print(silver_taxi1.get_fare())


main()