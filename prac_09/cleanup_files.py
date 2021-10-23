"""
CP1404 | Prac_09 | Dannielle Jones
Demos of various os module examples
"""
import os


def main():
    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Loop to rename the files
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            # full_name = os.path.join(directory_name, filename)
            # new_name = os.path.join(directory_name, new_name)
            # os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename
    if "_" not in new_name:
        new_name = list(new_name)
        for i, char in enumerate(new_name):
            if char == '.':
                break
            if char.isupper() and i != 0 and new_name[i-1] != " " and new_name[i-1] != "(":
                new_name[i] = f"_{char}"
        new_name = "".join(new_name)
        new_name = new_name.replace(".TXT", ".txt")
    if " " in new_name or (" " not in new_name and "_" not in new_name):
        new_name = new_name.title()
        new_name = new_name.replace(" ", "_").replace(".Txt", ".txt")
    return new_name


main()
