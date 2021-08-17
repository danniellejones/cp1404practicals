"""
CP1404 | Prac_01 Menus | Dannielle Jones

Pseudocode:
display menu
get choice
while choice != quit choice
    if choice == first choice
        do first task
    else if choice == second choice
        do second task
    else
        display invalid input error message
    display menu
    get choice
do final thing if needed
"""
MENU = "(H)ello \n(G)oodbye \n(Q)uit"

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
