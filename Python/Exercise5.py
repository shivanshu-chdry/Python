# Make a program which only print numeric numbers which are greater than 6
items = ['Shivanshu', 6, 25, 45, 2, 1, 3, 52, 49]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)