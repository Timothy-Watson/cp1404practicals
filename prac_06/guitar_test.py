"""
CP1404 practical - Guitar test
"""

from guitar import Guitar

# Test to see if guitar class works
guitar1 = Guitar("Guitar 1", 2002, 100)
guitar2 = Guitar("Guitar 2", 1942, 50000)

print(f"guitar 1 get_age() - Expected 22 got {Guitar.get_age(guitar1)}")
print(f"guitar 2 get_age() - Expected 82 got {Guitar.get_age(guitar2)}")

print(f"guitar 1 is_vintage() - Expected False got {Guitar.is_vintage(guitar1)}")
print(f"guitar 2 is_vintage() - Expected True got {Guitar.is_vintage(guitar2)}")
