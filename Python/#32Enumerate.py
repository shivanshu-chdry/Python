lst = ['Chicken', 'Burger', 'Pizza', 'Garlic Bread']

# i = 1
# for item in lst:
#     if i%2!=0:
#         print(item)
    
#     i = i + 1
# rather than writing this you can write
#here index will start from 0. That's why you have to do index%2==0. Rest of the things will stay the same.
for index, item in enumerate(lst):
    if index%2==0:
        print(item)