"""
CP1404 emails
Estimate: 10 min
Actual: 22 min
"""

name_to_email = {}
email = input("Email: ")
while email != '':
    # split the email at the '@' then split the first part at the '.' then join any list with a ' ' then titles
    name = " ".join(email.split('@')[0].split('.')).title()
    answer = input(f"Is your name {name}? (Y/N) ").lower()
    if answer != '' and answer != 'y':
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")
print()
for name, email in name_to_email.items():
    print(f"{name} ({email})")
