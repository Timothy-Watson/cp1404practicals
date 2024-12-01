"""
CP1404 Practical
A test program for the unreliable car class
"""
from unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("Range Rover", 100, 50)

# Repeat test program multiple times
for i in range(10):
    print("Distance travelled:", my_unreliable_car.drive(10))
    print(my_unreliable_car)
