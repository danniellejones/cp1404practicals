"""
CP1404 | Prac_03 | Dannielle Jones
Convert temperature between Celsius and Fahrenheit.
"""

MENU = """C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit \n>>> """


def main():
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        choice = input(MENU).upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
