"""
CP1404 practical - Project Management
estimated time - 60 min
   actual time - 130 min
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
        if choice == "L":  # Load projects
            filename = input("Enter a file name: ")
            projects = load_projects(filename)

        elif choice == "S":  # Save projects
            save_filename = input("Enter a file name to save to: ")
            save_projects(projects, save_filename)

        elif choice == "D":  # Display projects
            projects = sorted(projects)
            display_projects(projects)

        elif choice == "F":  # Filter projects by date
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            # Sort by date
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filtered_projects = filter_projects(date, projects)
            projects = sorted(projects, key=lambda x: x.start_date)  # Sort by start date
            for project in filtered_projects:
                print(project)

        elif choice == "A":  # Add new project
            new_project = add_new_project()
            projects.append(new_project)

        elif choice == "U":  # Update project
            for i, project in enumerate(projects):
                print(i, project)
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            project = projects[project_choice]
            update_project(project)

        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    choice = input("Would you like to save to projects.txt? ").lower()
    if choice in ["yes", "y", "yeah"]:  # many different yes options
        save_filename = input("Enter a file name to save to: ")
        save_projects(projects, save_filename)
    print("Thank you for using custom-built project management software.")


def save_projects(projects, filename):
    """Save projects to a specified filename"""
    out_file = open(filename, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=out_file)
    out_file.close()
    print(f"{len(projects)} projects saved to {filename}")


def update_project(project):
    """Updates the project if a value is given for the percent complete and priority"""
    try:
        new_percent = int(input("New percentage: "))
        project.completion_percentage = new_percent
    except ValueError:
        pass
    try:
        new_priority = int(input("New priority: "))
        project.priority = new_priority
    except ValueError:
        pass


def add_new_project():
    """Adds a new project with error checking"""
    print("Let's add a new project")
    name = input("Name: ")
    while name == "":
        print("No name given")
        name = input("Name: ")

    is_valid_input = False
    while not is_valid_input:
        try:
            start_date_string = input("Start date (dd/mm/yyyy): ")
            start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
            is_valid_input = True
        except ValueError:
            print("Not a valid date")

    is_valid_input = False
    while not is_valid_input:
        try:
            priority = int(input("Priority: "))
            is_valid_input = True
        except ValueError:
            print("Not a valid number")

    is_valid_input = False
    while not is_valid_input:
        try:
            cost = float(input("Cost estimate: $"))
            is_valid_input = True
        except ValueError:
            print("Not a valid cost")

    is_valid_input = False
    while not is_valid_input:
        try:
            percent_complete = int(input("Percent complete: "))
            is_valid_input = True
        except ValueError:
            print("Not a valid number")

    return Project(name, start_date, priority, cost, percent_complete)  # Ignore lines, variable will be referenced


def filter_projects(date, projects):
    """Filter projects if they are started after date"""
    filtered_projects = []
    for project in projects:
        if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date:
            filtered_projects.append(project)
    # The sample output might be wrong because you say to sort by projects that start AFTER the date.
    # In the example it shows a project the starts on the date given.
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
    try:  # Only execute if the filename exists
        in_file = open(filename, "r")
        in_file.readline()  # reads the header of the file
        for line in in_file:
            parts = line.strip().split("\t")  # uses tabs to separate project parts
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
        in_file.close()
        print(f"{len(projects)} projects loaded from {filename}")
    except FileNotFoundError:
        print("File not found")
    return projects


main()
