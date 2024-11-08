"""
CP1404 practical - Guitar
This is a program that uses the guitar class
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of guitars, save as objects, display, add new guitars."""
    guitars = []
    load_guitars(guitars)
    # Print both unsorted and sorted list of guitars
    print("Unsorted guitars")
    for guitar in guitars:
        print(guitar)
    print("\nSorted guitars by year")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    print("\nAdd new guitars:")
    add_guitars(guitars)

    write_guitars(guitars)


def write_guitars(guitars):
    """Writes guitars to file"""
    out_file = open(FILENAME, "w")
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()


def add_guitars(guitars):
    """Asks the user for details for the guitars and adds them to the guitars."""
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{name} ({year}) : ${cost:.2f} added.")
            print("\nAdd new guitars:")
            name = input("Name: ")
        except ValueError:
            print("Incorrect value")
        except NameError:
            print("No value given")


def load_guitars(guitars):
    """Loads guitar from guitars CSV."""
    in_file = open(FILENAME, 'r')
    for line in in_file:
        # print(repr(line))  # Debugging
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


main()
