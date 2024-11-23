"""
CP1404 Practical
A test program for the silver service taxi class
"""
from silver_service_taxi import SilverServiceTaxi

my_silver_service_taxi = SilverServiceTaxi("Phantom", 200, 4)

print(my_silver_service_taxi)
my_silver_service_taxi.drive(9)
print(my_silver_service_taxi)
print(f"Your {my_silver_service_taxi.current_fare_distance}km journey will cost ${my_silver_service_taxi.get_fare()} with a fanciness of {my_silver_service_taxi.fanciness}")
