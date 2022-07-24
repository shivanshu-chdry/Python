l = 10 #Global Variable are those variables which can be used anywhere in the program and has an infinite scope
def function1(n):
    # l = 5 #This is a local variable. If you want to change the value of a variable in a function you can write that variable again. These variables can't be printed outside the function
    global l #You can change the value of global variable like this
    l = l +45
    print(l)
    print(n, 'I have printed it')

function1('Football')

#This is a nested function(Function inside function)
def function2():
    s = 20
    def shivanshu():
        global s
        s = 88 #Here the variable will not be changed to 88 because the global variable search outside the function. And there was no s variable so it ignored the line
    print('Before calling Shivanshu()', s)
    shivanshu()
    print('After calling Shivanshu()', s)
function2()
print(s)
