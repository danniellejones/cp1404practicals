"""
CP1404 | Prac_04 | Dannielle Jones
Lottery ticket generator.
"""
import random

QUICK_PICKS = []

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick_numbers = []
    for j in range(6):
        number = random.randint(1, 45)
        while number in quick_pick_numbers:
            number = random.randint(1, 45)
        quick_pick_numbers.append(number)
        quick_pick_numbers.sort()
    QUICK_PICKS.append(quick_pick_numbers)

for quick_pick in QUICK_PICKS:
    for number in quick_pick:
        print("{:2}".format(number), end=" ")
    print()
