# Make an input program which asks the user for it's age and tells them whether they are elegible to drive
#Solution:
print('Enter your age')
age = int(input())

if age>18 and age<100:
    print('You are Eligible to drive')

elif age>7 and age<18:
    print('You are not Eligible to drive')

elif age==18:
    print('It can only be decided by your physical checkup. Please book an appointment on our website www.carlicense.com')

else:
    print('Enter a valid age')