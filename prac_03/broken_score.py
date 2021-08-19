"""
CP1404 | Prac_03 | Dannielle Jones
Get score and determine score result.
"""
import random


def main():
    # Get user to enter score and print result
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    # Get a random score and print the result
    score = random.randint(0, 100)
    result = determine_result(score)
    print("Random Score: {} - Result: {}".format(score, result))


def determine_result(score):
    """Determine the result of the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
