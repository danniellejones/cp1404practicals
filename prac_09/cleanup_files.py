"""
CP1404 | Prac_09 | Dannielle Jones
Use os modules to rename files to a specific format.
"""
import os


def main():
    """Rename files within subdirectories to a 'fixed' version."""
    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        # Loop to rename the files
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = list(filename)
    for i, char in enumerate(new_name):
        if char.isupper() and i != 0:
            if new_name[i - 1] != " " and new_name[i - 1] != "(" and new_name[i - 1] != "_(":
                new_name[i] = char.replace(char, f"_{char}")
        if not char.isupper() and new_name[i-1] == " " or i == 0 or new_name[i-1] == "(" or new_name[i-1] == "_":
            new_name[i] = char.upper()
        if char == " ":
            new_name[i] = char.replace(" ", "_")
        if char == "(" and new_name[i-1] != "_":
            new_name[i] = char.replace(char, f"_{char}")
        if char == '.':
            break
    new_name = "".join(new_name)
    new_name = new_name.replace(".TXT", ".txt")
    return new_name


main()
