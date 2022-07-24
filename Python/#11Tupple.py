from re import A


numbers = [2, 5, 8, 12, 15, 52]
numbers[2] = 7
print(numbers)

#Mutable - Can change
#Immutable - Cannot change

tp = (2, 85, 45, 23, 12)
print(tp)
#tp[1] = 8 This is wrong because the value of tupple cannot be changed. Tupples are Immutable

a = 5
b = 4
#There are two methods if you want to interchange the values of these two variables
a, b = b, a
print(a,b)
temp = a
a = b
b = temp
print(a,b)