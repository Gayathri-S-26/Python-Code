import re

phone_regex = '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'
phone_number = input("Enter Phone number: ")
match = re.search(phone_regex, phone_number)

if match is not None:
    print("It is a Valid Phone Number")
else:
    print("It is not a Valid Phone Number")