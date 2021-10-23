"""
CP1404 | Prac_09 | Dannielle Jones
Use shutil module to move files into new directories.
"""
import os
import shutil


def main():
    """Sort files into directories named according to their extensions."""
    os.chdir('FilesToSort')
    # Read the extensions from available files
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        extension = get_extension(filename)
    # Make a new directory
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
    # Move file to new directory
        shutil.move(filename, f'{extension}/')


def get_extension(filename):
    """Get the extension from a filename."""
    for i, char in enumerate(filename):
        if char == ".":
            extension = filename[i+1:]
    return extension


main()
