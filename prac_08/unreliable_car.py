"""
CP1404 | Prac_08 | Dannielle Jones

"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car that inherits from Car."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{} reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
