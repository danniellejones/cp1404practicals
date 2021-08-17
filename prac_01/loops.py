"""CP1404 | Prac_01 Loops | Dannielle Jones"""

# Display the odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Count in 10's from 0 to 100'
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Ask user for a number and print that many stars on one line
number = int(input("Number of stars: "))
for i in range(number):
    print("*", end="")

# Print n lines of increasing stars using the number above
for i in range(number + 1):
    print("*" * i)
print()
