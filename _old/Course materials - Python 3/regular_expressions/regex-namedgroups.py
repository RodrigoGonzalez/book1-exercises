import re

string = "Michael Herman"

if m := re.match(r"(?P<first>\w+)\W+(?P<last>\w+)", string):
    print("group(0) : ", m.group(0))
    print("group(1) : ", m.group(1))
    print("group(2) : ", m.group(2))
    print("")
    print('group("first") : ', m.group("first"))
    print('group("last") : ', m.group("last"))
else:
    print("Sorry. No match!!")
