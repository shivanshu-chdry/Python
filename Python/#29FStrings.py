#String Formatting
import math
me = 'Shivanshu'
a1 = 3
# a = 'this is %s'%me
a = 'This is {1} {0}' #You can even change the location of words by putting numbers in the curly brackets
b = a.format(me, a1)
print(b)
# or
c = f'This is {me} {a1} {math.cos(65)}' #You can also use modules
print(c)