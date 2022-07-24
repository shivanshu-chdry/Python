#Generators
'''
Iterable - __iter__() or __getitem__()
Iterator - __next__
Iteration - The process to iterate is known as Iteration
'''

for i in range(78): #Range is a type of generator so i can only run it one time
    print(i)

#Making your own generator

def gen(n):
    for i in range(n):
        yield i #Yield is a generator

def newrange(a):
    for i in range(a):
        yield i

