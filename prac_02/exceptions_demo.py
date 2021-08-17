"""
CP1404 | Prac_02 Exceptions Demo | Dannielle Jones
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero")
        else:
            valid_input = True
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
print("Finished.")

"""
Questions:
1. When will a ValueError occur?
    - When a user inputs a non-integer into the numerator or denominator
    
2. When will a ZeroDivisionError occur?
    - When a user enters a zero in the denominator
    
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, by adding a while statement and decision structure (exception has been commented out)
"""