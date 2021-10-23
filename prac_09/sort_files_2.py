"""
CP1404 | Prac_09 | Dannielle Jones
Use shutil module to move files based on user categorisation system.
"""
import os


def main():
    """Sort files into directories named according to their extensions."""
    os.chdir('FilesToSort')
    extension_to_category = {}
    # Read the extensions from available files
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        extension = filename.split(".")[-1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_to_category[extension] = category
        # Make a new directory
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        # Move file to new directory
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
