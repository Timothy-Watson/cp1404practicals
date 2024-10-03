"""
CP1404/CP5632 - Practical
Different file
"""
FILENAME01 = "name.txt"
FILENAME02 = "numbers.txt"


def program01():
    """Gets a name and prints it to a file"""
    name = input("Name: ")
    out_file = open(FILENAME01, 'w')
    print(name, file=out_file)
    out_file.close()


def program02():
    """Read a file and print the contents"""
    in_file = open(FILENAME01, 'r')
    print(f"Hi {in_file.readline().strip()}!")
    in_file.close()


def program03():
    with open(FILENAME02) as in_file:
        result = int(in_file.readline()) + int(in_file.readline())
        print(result)


def program04():
    total = 0
    with open(FILENAME02) as in_file:
        for line in in_file:
            total = total + int(line)
    print(total)


program01()
program02()
program03()
program04()
