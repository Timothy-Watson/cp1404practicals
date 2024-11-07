"""
CP1404 practical - Programming Languages
expected time to complete - 45 min
start time - 9:41PM
finish time - 9:57PM
time to complete - 16 min
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        return str(self)

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
