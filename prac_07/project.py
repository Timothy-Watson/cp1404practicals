"""
CP1404 practical - project class
"""


# Things in project: Name, Start Date,Priority, Cost Estimate, Completion Percentage
class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Load values"""
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        return f"{vars(self)}"

    def __str__(self):
        return f"{self.name}: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, completion: {self.completion_percentage}"

    def __lt__(self, other):
        return self.priority < other.priority

