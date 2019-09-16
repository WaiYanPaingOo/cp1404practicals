import random
from prac_08.car import Car


class UnReliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):

        return "{}, reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("Cannot Drive")
            distance_driven = 0
            return distance_driven