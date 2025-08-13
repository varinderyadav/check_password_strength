import re

password = input("Enter your password: ")


pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"

if re.match(pattern, password):
    print("Yes! your Password is Strong ")
else:
    print("Weak Password")


























