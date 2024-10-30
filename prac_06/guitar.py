"""
CP1404 practical - Guitar
expected time to complete - 30 min
start time - 10:00PM
finish time - PM
time to complete -  min
"""
import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return 2024 - self.year

    def is_vintage(self):
        if Guitar.get_age(self) >= 50:
            return True
        else:
            return False

