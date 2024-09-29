MINIMUM_LENGTH = 5
password = input("Password: ")

while len(password) < MINIMUM_LENGTH:
    print("Invalid password")
    password = input("Password: ")
print("*" * len(password))
