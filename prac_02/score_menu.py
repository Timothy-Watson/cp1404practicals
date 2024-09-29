"""
CP1404 practical
score program with a menu

Menu:
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""

MENU = f"(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid Input")
        print(MENU)
        choice = input(">>>").upper()
    print("Farewell!")


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
