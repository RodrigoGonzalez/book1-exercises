import re

string = "My name is Michael Herman"

if m := re.match(r'(.*) name (.[s]?) .*', string):
    print("group(0): ", m.group(0))
    print("group(1): ", m.group(1))
    print("group(2): ", m.group(2))
else:
    print("Sorry. No match!!")
