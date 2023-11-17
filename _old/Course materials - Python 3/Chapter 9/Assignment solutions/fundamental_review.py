# 9.3 fundamental_review.py
# Reviewing the Fundamentals:
# functions, loops, lists, dicts, and conditional logic

print("\n# -- part 1 -- #")

# Modify the variable value so that all of the `print` statements return `True`.

zero = 0
one = 23
two = [5, 4, 3, 2, 1]
three = ["I", "love", "Python!"]
four = [["P", "y", "t", "h", "o", "n"], ["i", "s"], ["f", "u", "n"]]
five = {"happy": "birthday", "fish": "chips", "day": "night"}
six = {1, 2, 3, 4, 5}
days = ("Mon", "Tue", "Wed")
x, y, seven = days

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# -------------------------------------- #

print(f"zero:  {zero == 0}")
print(f"one:   {one > 22}")
print(f"two:   {len(two) == 5}")
print(f'three: {three[2] == "Python!"}')
print(
    f"""four:  {four[0][5] == 'n' and four[0][0] == "P" and four[2][1] == "u"}"""
)
print(f'five:  {five.get("fish") == "chips"}')
print(f"five:  {len(five) == 3}")
print(f"six:   {len(six & {2, 5, 7}) == 2}")
print(f'seven: {seven == "Wed"}')

# -------------------------------------- #

print("\n# -- part 2 -- #")

# Find a value for the `value` variable so that all print statements return True

value = [1, 1, 1, 1]

# DO NOT CHANGE ANYTHING BELOW THIS LINE #
# ------------------------------------ #

if type(value) is list:
    print(True)
else:
    print(False)

for x in value:
    if type(x) is not int:
        print(False)
    else:
        print(True)

num = 0
while num < value[2]:
    print(True)
    num += 1

for y in range(value[3]):
    if y in value:
        print(False)

try:
    value[5] = "Cat"
    while True:
        print(False)
except IndexError:
    print(True)

try:
    assert value[3] == -1
except AssertionError:
    print(True)

# -------------------------------------- #
