#1. How can we access and print the docstring of a function.
def function1():
    '''This is the docstring of this function'''

print(function1.__doc__)

#2. Make a fibonachi calculating system
def fibonachi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    
num = int(input("Enter a number\n"))
print(fibonachi(num))
