"""
CP1404 | Prac_02 Exceptions to Complete | Dannielle Jones
Checks for a valid input (integer) and prints result
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
