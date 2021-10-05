"""
CP1404 | Prac_08 | Dannielle Jones
Silver service taxi client program.
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

silver_taxi_1 = SilverServiceTaxi(100, "Hummer", 2)
silver_taxi_1.drive(18)
print(silver_taxi_1)
print("Fare: ${:.2f}".format(silver_taxi_1.get_fare()))
