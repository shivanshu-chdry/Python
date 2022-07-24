#Lambda or anonymous functions are one line functions
minus = lambda x,y: x-y
#is same as:
def minus1(x, y):
    return x-y

print(minus(9, 4))
print(minus1(9, 4))

#Sort Function
# def a_first(a):
#     return a[1]
#or
a = [[1, 14], [2, 5], [48, 24]]
a.sort(key=lambda a:a[1]) #This will sort the list
print(a)
