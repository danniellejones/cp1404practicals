"""
CP1404 | Prac_04 | Dannielle Jones
Data file lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def print_subject_details(data):
    for record in data:
        print("{} is taught by {} and has {} students".format(record[0], record[1], record[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)
    input_file.close()
    # print(data)  # Checks if parts has been added to the list
    return data


main()
