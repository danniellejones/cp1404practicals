"""
CP1404 | Prac_03 | Dannielle Jones
Get a password and checks that it is longer than the minimum required length.
"""
MIN_LENGTH = 10


def main():
    password = get_password(MIN_LENGTH, "Password must be at least {} characters long".format(MIN_LENGTH))
    print_asterisks(password)


def print_asterisks(password):
    print(len(password) * "*")


def get_password(min_length, error_message):
    password = input("Password: ")
    while len(password) < min_length:
        print(error_message)
        password = input("Password: ")
    return password


main()
