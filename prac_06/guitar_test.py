"""
CP1404 | Prac_06 | Dannielle Jones
Guitar test program using Guitar class.
"""
from guitar import Guitar


guitar1 = Guitar("Gibson L-5", 1922, 16035.40)
print(guitar1.get_age())
print(guitar1.is_vintage())
print(guitar1)
guitar2 = Guitar("Slayer OMG", 1971, 2000)
print(guitar2.get_age())
print(guitar2.is_vintage())
print(guitar2)
