"""
CP1404 | Prac_06 | Dannielle Jones
Use ProgrammingLanguage class to make a list of programming languages.
"""
from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print("{} \n{} \n{}".format(ruby, python, visual_basic))

# Create a list of programming languages
programming_languages = [ruby, python, visual_basic]

# List dynamic programming languages using a for loop and is_dynamic method
print("The dynamically typed languages are: ")
for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.field)
