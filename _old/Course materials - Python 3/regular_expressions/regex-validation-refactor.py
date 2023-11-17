import re

validation = re.compile(r'[A-Za-z0-9.]+@[A-Za-z0-9.]+.com$')

email = input("Please enter your email address: ")

while not validation.search(email):
    print("Please enter your email address correctly!")
    email = input("Please enter your email address: ")

print(f"\nYour email address is {email}!")
