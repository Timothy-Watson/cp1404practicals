"""
CP1404/CP5632 - Practical
Random number between 1 and 100 inclusive.
"""
import random

print(random.randint(5, 20))  # line 1, I got the number "5". The smallest and largest numbers I can see are 5 and 20
print(random.randrange(3, 10, 2))  # line 2, I got the number "9". Smallest and largest numbers are 3 and 9.
# Line 2 cannot produce a 4 as it counts in 2s and starts at 3, so it is all odd numbers.
print(random.uniform(2.5, 5.5))  # line 3, I got the number "3.7700981719816413".
# The smallest and largest numbers this code can receive is 2.5000000000000000 and 5.5000000000000000.

