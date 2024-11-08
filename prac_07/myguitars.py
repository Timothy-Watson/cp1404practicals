"""
CP1404 practical - Guitar
This is a program that uses the guitar class
"""

from guitar import Guitar


def main():
    """Read file of guitars, save as objects, display"""
    guitars = []
    load_guitars(guitars)
    print("Unsorted guitars")
    for guitar in guitars:
        print(guitar)
    print("\nSorted guitars by year")
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_guitars(guitars):
    """Loads guitar"""
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        # print(repr(line))  # Debugging
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()


main()
