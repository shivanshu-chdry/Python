#Functions are of two types: built-in function and user defined function
a = 9
b = 8
c = sum((a, b)) #sum is a built-in function
print(c)

#User Defined Function
def function1 (a, b):
    print('This is function1', a+b)

function1(5, 7)

def function2 (a,b):
    '''This is a function used to calculate the average of two numbers and this function doesn't work for three
numbers''' #This is a docstring which is the first line of a function used to identify that function. It could be a warning a note or something else. It's not like multi-line comment
    average = (a+b)/2
    print(average)
    return average

var = function2(5, 7)
print(var)
print(function2.__doc__) #You can print the docstring of a function like this