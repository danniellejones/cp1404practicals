"""
CP1404 | Prac_06 | Dannielle Jones
Class for a programming language.
"""


class ProgrammingLanguage:

    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
