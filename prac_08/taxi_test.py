"""
CP1404 | Prac_08 | Dannielle Jones
Test Taxi class.
"""
from prac_08.taxi import Taxi

taxi_1 = Taxi(100, "Prius 1")
taxi_1.drive(40)
print(taxi_1)
print("Fare: ${:.2f}".format(taxi_1.get_fare()))
taxi_1.start_fare()
taxi_1.drive(100)
print("Fare: ${:.2f}".format(taxi_1.get_fare()))
print(taxi_1)
