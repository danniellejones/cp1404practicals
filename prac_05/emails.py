"""
CP1404 | Prac_05 | Dannielle Jones
Get email, extract name and store in dictionary.
"""


def main():
    """Create dictionary of emails-to-names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        correct = input("Is your name {}? (Y/n) ".format(name))
        if correct.upper() != "Y" and correct != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Get predicted name from email."""
    prefix = email.split("@")
    parts = prefix[0].split(".")
    name = " ".join(parts).title()
    return name


main()
