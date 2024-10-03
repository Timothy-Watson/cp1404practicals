"""Password star program"""
MINIMUM_LENGTH = 5


def main():
    password = get_password()
    print_hidden_password(password)


def print_hidden_password(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Password: ")
    return password


main()
