'''
Operators in Python:
Arithmetic Operator
Assignment Operator
Comparison Operator 
Logical Operator 
Identity Operator
Membership Operator
Bitwise Operator
'''

#Arithmetic Operators help in performing mathematical operations
print('{Arithmetic Operators}')
print('5 + 6 is',5+6)
print('5 - 6 is',5-6)
print('5 * 6 is',5*6)
print('5 **6 is',5**6) # ** gives the exponential power
print('5 / 6 is',5/6)
print('5//6 is',5//6) #// gives integer value
print('11%5 is',11%5) # % gives the remainder

#Assignment Operators assign some value to the variable
print('{Assignment Operators}')
x = 5 #Here '=' is assigning a value in x
print(x)
x += 5 #This adds something in the variable
# x-= 5
# x/= 5
# x% = 5
#And many more... you can search about them on internet
print(x)

#Comparison Operators compare two values
print('{Comparison Operators}')
i = 5
print(i==6) #Here == is used for comparing. i is not five that's why the program is returning false which is a boolean value
print(i != 6) # != means not equal to. Here the program will return true
print(i>6)
print(i<6)
print(i >= 5)
print(i <= 5)

#Logical Operators 
print('{Logical Operators}')
a = True
b = False
print(a and a) #It's returning true because both the variables entered here are true
print(a and b) #It's returning false because one variable is false
print(a or b) #It's returning true because one of the variable is true

#Identity Operators are is and is not
print('{Identity Operators}')
r = True
w = False
print(r is w)
print(r is not w)

#Membership Operators are in and not in
print('{Membership Operators}')
list = [1, 2, 3, 4, 58, 6, 75, 45, 49]
print(49 in list) #It'll return true because 49 is in the list
print(49 not in list)

#Bitwise Operators it works with binary numbers
print('{Bitwise Operators}')
#Numbers in Binary:
#0 - 00
#1 - 01
#2 - 10
#3 - 11
print(0 & 1) #It'll print 0 because:
'''
0 in binary - 00
1 in binary - 01
              00 = 0
'''
print(0 | 3) #It'll print 3 because:
'''
0 in binary - 00
3 in binary - 11
              11 = 3
'''