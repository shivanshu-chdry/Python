#For Loops
list = [['Shivanshu', 5], ['Sarthak', 50] , ['Ojas' ,250], ['Prabhat', 25]]
for items, lays in list:
    print(items, lays) #It can be used in lists like this

dict = {'Shivanshu':10, 'Sarthak':500, 'Ojas':10000, 'Prabhat':50}
for items, lays in dict.items():
    print(items, lays) #It can be used in dictionaries like this 

#While Loops
#This loop will run until the condition is true
i = 0

while (i<45):
    print(i, end = ' ')
    i = i + 1