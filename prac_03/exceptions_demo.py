"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when a non integer value is given, this can include string ("Tim") or float (3.5).
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the program tries to divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes you can, you can create a while loop to make sure the denominator isn't 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
