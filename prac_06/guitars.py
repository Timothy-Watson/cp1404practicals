"""
CP1404 practical - Guitar
expected time to complete - 30 min
start time - 10:00PM
finish time - 10:53PM
time to complete - 53 min
"""

from guitar import Guitar

guitars = []
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print("My guitars")
name = input("Name: ")
while name != "":
    try:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")
    except ValueError:
        print("Incorrect value")
    except NameError:
        print("No value given")

print("\n... snip ...\n")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if Guitar.is_vintage(guitar) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")