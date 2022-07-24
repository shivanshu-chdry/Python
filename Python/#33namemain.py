from imp import init_builtin
from mimetypes import init

from pip import main


def shivanshu(str):
    print(f'the string is {str}')

def sum(num1, num2):
    print(num1 + num2 + 54)

#if __name__ == '__main__': #Sometimes when you import a file to another you may face some problem. Like if you run a function it'll execute the whole program to prevent this you can use name=main function
print(shivanshu('Shivanshu'))
o = sum(6, 4)
print(sum)