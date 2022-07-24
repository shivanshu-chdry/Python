#If you don't want error and wanna jump to 10th line
print('Enter first number')
num1 = input()
print('Enter second number')
num2 = input()
try:
    print('The sum of these two numbers is',int(num1) + int(num2))
except Exception as e:
    print(e)
print('This line is very important')