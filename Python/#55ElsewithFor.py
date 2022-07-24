food =['Chicken', 'Pizza', 'Garlic Bread']
#Python will go inside else if the for loop ends normally
for item in food:
    print(item)
    

else:
    print('This for loop ended normally')


for item in food:
    print(item)
    break

else:
    print('This for loop ended with a break statement')


for item in food:
    if item == 'Mutton': #Here else statement will be printed because Mutton is not in list. So, it'll ignore break
        break

else:
    print('This for loop ended normally')