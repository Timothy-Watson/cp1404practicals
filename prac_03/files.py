"""
CP1404/CP5632 - Practical
Different file
"""
FILENAME = "name.txt"


def program01():
    """Gets a name and prints it to a file"""
    name = input("Name: ")
    out_file = open(FILENAME, 'w')
    print(name, file=out_file)
    out_file.close()


def program02():
    """"""
    in_file = open(FILENAME, 'r')
    print(f"Hi {in_file.readline().strip()}!")
    in_file.close()


def program03():
    pass


program01()
program02()
