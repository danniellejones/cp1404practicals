"""
CP1404 | Prac_04 | Dannielle Jones
Basic list operations and username security checker.
"""

# 1. Basic list operations
numbers = []
total = 0
for i in range(5):
    number = int(input("Number: "))
    total += number
    numbers.append(number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(total / len(numbers)))

# 2. Woefully inadequate security checker (case sensitive)
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access denied")
