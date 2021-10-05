"""
CP1404 | Prac_08 | Dannielle Jones
Unreliable car test client program.
"""
from prac_08.unreliable_car import UnreliableCar

# Should return being driven.
unreliable_car_1 = UnreliableCar(90, "Prius 1", 100)
print(unreliable_car_1)
unreliable_car_1.drive(20)
print(unreliable_car_1)

# Should return not being driven.
unreliable_car_1 = UnreliableCar(90, "Prius 1", 0)
print(unreliable_car_1)
unreliable_car_1.drive(20)
print(unreliable_car_1)

# Should vary being driven or not.
unreliable_car_1 = UnreliableCar(90, "Prius 1", 50)
print(unreliable_car_1)
unreliable_car_1.drive(20)
print(unreliable_car_1)
