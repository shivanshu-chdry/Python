def function1():
    print('My name is shivanshu')

func2 = function1 
func2()

#A function which return functions
def funcret(num):
    if num==0:
        return print
    elif num==1:
        return sum

func = funcret(1)
print(func)

def executor(func1):
    func1('This')

executor(print)

#Function inside function
def dec1(funct):
    def nowexec():
        print('Executing...')
        funct()
        print('Executed')
    return nowexec
#@dec1 can also be used at the place of who_are_you = dec1(who_are_you)
def who_are_you():
    print('Human')

who_are_you = dec1(who_are_you) #who_are_you will become a part of dec1 and will be printed at the place of funct()
who_are_you()