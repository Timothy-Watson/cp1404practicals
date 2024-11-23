"""
CP1404 Practical
unreliable car class
"""
from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        if self.reliability > randint(0, 100):
            return super().drive(distance)
        else:
            return 0
