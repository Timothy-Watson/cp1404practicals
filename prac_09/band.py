"""
CP1404 Practical
Band class
"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string of the band and its musicians."""
        musician_string = ""
        for musician in self.musicians:
            musician_string += f"{musician.name} ({musician.instruments})"
        return f"{self.name} ({musician_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Each musician plays their instrument if they have one."""
        for musician in self.musicians:
            print(musician.play())
        # I really need help figuring out why a "None" is printed at the very end of the program
        # I tried using debugger and other things and I cannot figure it out
