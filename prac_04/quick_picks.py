"""CP1404 Practical - Quick Picks"""

import random

RANDOM_LOW = 1
RANDOM_HIGH = 45
NUMBER_OF_PICKS = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        picks = []
        for j in range(NUMBER_OF_PICKS):
            random_number = random.randint(RANDOM_LOW, RANDOM_HIGH)
            while random_number in picks:
                random_number = random.randint(RANDOM_LOW, RANDOM_HIGH)
            picks.append(random_number)
        picks.sort()
        for pick in picks:
            print(f"{pick:2}", end=" ")
        print()



main()
