"""
CP1404 practical - Project Management
estimated time - 60 min
    start time - 10:30 PM
      end time -
   actual time -
"""

import datetime
from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Project program with many options"""
    filename = "projects.txt"  # set default filename

    print("Welcome to Pythonic Project Management")
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a file name: ")
            load_projects(filename)
        elif choice == "S":
            pass
        elif choice == "D":
            projects = sorted(projects, key=lambda x: x.priority)
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            projects = sorted(projects, key=lambda x: x.start_date)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = filter_projects(date, projects)
            for project in filtered_projects:
                print(project)
        elif choice == "A":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def add_new_project():
    """Adds a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    return Project(name, start_date, priority, cost, percent_complete)


def filter_projects(date, projects):
    """Filter projects if they are started after date"""
    filtered_projects = []
    for project in projects:
        if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date:
            filtered_projects.append(project)
    # The sample output is wrong because you say to sort by projects that start AFTER the date.
    # In the example it shows a project the starts on the date
    return filtered_projects


def display_projects(projects):
    """Loads and displays projects sorted by priority and grouped by completion"""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.completion_percentage == 100:
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Complete projects:")
    for project in complete_projects:
        print(project)


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
