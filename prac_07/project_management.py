"""
CP1404 practical - Project Management
estimated time - 60 min
    start time - 10:30 PM
      end time -
   actual time -
"""

import datetime
from project import Project

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(projects)


def load_projects(filename):
    """Load"""
    projects = []
    in_file = open(filename, "r")
    in_file.readline()  # reads the header of the file
    for line in in_file:
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    in_file.close()
    return projects


main()
