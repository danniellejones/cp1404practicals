"""
CP1404 | Prac_03 | Dannielle Jones
Get a password and checks that it is longer than the minimum required length.
"""

MIN_LENGTH = 10
password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Password must be at least {} characters long".format(MIN_LENGTH))
    password = input("Password: ")
print(len(password) * "*")
