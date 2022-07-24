'''
Comprehensions:
List
Dictionary
Set
Generator
'''
#List Comprehensions

# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
#You can write all this code in one line using comprehensions
ls = [i for i in range(100) if i%3==0]
print(ls)

#Dictionary Comprehensions

#If I want to write these items from 0 to 100 I can either write it like this which is time consuming or I can use comprehensions for that.
# dict1 = {1:'Item1',  2:'Item2'}
dict1 = {i:f'Item {i}' for i in range(100)}
print(dict1)

#Set Comprehensions

dresses = {dress for dress in ['Dress1', 'Dress2', 'Dress1', 'Dress2']} #Set take a value only one time. So, Dress1 and Dress2 will be printed once only
print(dresses)

#Generator Comprehensions

evens = (i for i in range(100) if i%2==0)

for item in evens:
    print(item)