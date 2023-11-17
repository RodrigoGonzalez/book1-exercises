# 6.3 review exercises


# print the integer 2 through 10 using a "for" loop
for i in range(2, 11):
    print(i)


for i in range(2, 11):
    print(i)


def doubles(num):
    ''' Return the result of multiplying an input number by 2 '''
    return num * 2

# Call doubles to double the number 2 three times
my_num = 2
for _ in range(0, 3):
    my_num = doubles(my_num)
    print(my_num)
