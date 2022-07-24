#Map Function is a function which can be applied on the whole list
numbers = ('3', '45', '25')
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# It's not good to run for loops again and again in a code. That's why we use map function.
numbers = list(map(int, numbers))

numbers[2] = numbers[2] + 1
print(numbers[2])

#You can also use them like
# def sq(a):
#     return a*a

# lst = [2, 56 ,3, 45, 6, 89, 7]
# square = list(map(sq, lst))
# print(square)

def square(a):
    return a*a

def cube(a):
    return a*a*a


func = [square, cube]

for i in range(5):
    x = list(map(lambda s:s(i), func))
    print(x)

#Filter Function
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_greater(num):
    return num>5

gr_5 = list(filter(is_greater, lst))
print(gr_5)

#Reduce Function. It is a module of functools
from functools import reduce
lst1 = [1, 2, 3, 4]
# num = 0
# for i in lst1():
#     num = num + i
#You can do it like:
num = reduce(lambda x,y:x+y, lst1)
print(num)
