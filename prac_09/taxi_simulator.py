"""
CP1404 Practical
Taxi Simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main menu for taxi simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            current_taxi = get_valid_taxi(taxis)

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                pass

        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def get_valid_taxi(taxis):
    """Returns a valid taxi from the taxi list"""
    valid_taxi = False
    while not valid_taxi:
        try:
            taxi_number = int(input("Choose taxi: "))
            if taxi_number >= len(taxis) or taxi_number < 0:
                print("Invalid taxi choice")
            else:
                valid_taxi = True
        except ValueError:
            print("Invalid taxi choice")
    return taxis[taxi_number]  # Will always return a valid taxi number


main()
