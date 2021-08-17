"""
CP1404 | Prac_01 Sequences | Dannielle Jones
Program that determines the even, odd and squares of numbers from x through to y (input from user)
"""

MENU = "(E)ven \n(O)dd \n(S)quares \n(Q)uit \n>>> "

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
choice = input(MENU).upper()
while choice != "Q":
    if choice == "E":
        # Show the even numbers from x to y
        for i in range(x, y+1):
            if i % 2 == 0:
                print(i, end=" ")
        print()
    elif choice == "O":
        # Show the odd numbers from x to y
        for i in range(x, y+1):
            if i % 2 == 1:
                print(i, end=" ")
        print()
    elif choice == "S":
        # Show the squares from x to y
        for i in range(x, y+1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    choice = input(MENU).upper()
print("Finished.")
