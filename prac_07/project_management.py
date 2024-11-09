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
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (Q)uit"""


def main():
    """Project program with many options"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def load_projects(filename):
    """Load and save projects from a file"""
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
