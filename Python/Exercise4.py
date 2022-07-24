# Make a faulty calculator which will perform all the calculations correctly except:
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4 

print('Welcome to calc!')
sign = input('What operation you want me to perform on these numbers:')
num1 = input('Enter your first number:')
num2 = input('Enter your second number:')
faultydict = {"45*3":"555", "56+9":"77", "56/6":"4"}
expression = num1 + sign + num2
reverse = num2 + sign + num2
if expression in faultydict.keys():
    print(faultydict[expression])
    pass

elif reverse in faultydict.keys():
    print(reverse[expression])
    pass

else:
    print(eval(num1 + sign + num2))