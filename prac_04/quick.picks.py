"""
CP1404 | Prac_04 | Dannielle Jones
Lottery ticket generator.
"""
import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Generate lottery quick picks from random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("You cannot generate negative quick picks.")
        number_of_quick_picks = int(input("How many quick picks? "))

    quick_picks = []
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
            quick_pick.sort()
        quick_picks.append(quick_pick)
    print_quick_picks(quick_picks)


def print_quick_picks(quick_picks):
    """Print quick pick numbers."""
    for quick_pick in quick_picks:
        for number in quick_pick:
            print("{:2}".format(number), end=" ")
        print()


main()
