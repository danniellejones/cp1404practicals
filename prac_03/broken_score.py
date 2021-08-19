"""
CP1404/CP5632 - Practical 1 - Dannielle Jones
Get score and determine score result.
"""


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


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
