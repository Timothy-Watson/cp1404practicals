"""
CP1404 practical - Guitar
This is a guitar class
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return 2024 - self.year

    def is_vintage(self):
        if Guitar.get_age(self) >= 50:
            return True
        else:
            return False
