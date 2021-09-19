"""
CP1404 | Prac_06 | Dannielle Jones

"""
from guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added.")
    # Same as above but does not utilise string method from Guitar class
    # guitars.append(Guitar(name, year, cost))
    # print("{} ({}) : ${:,.2f} added.".format(name, year, cost))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))  # Test data
    # guitars.append(Guitar("Gibson", 1971, 700.50))  # Test data
    name = input("Name: ")
print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost,
                                                               vintage_string))
