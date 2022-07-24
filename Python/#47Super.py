#Super() and Overriding

class A:
    classvar1 = 'I\'m a class variable in class A'
    def __init__(self):
        self.var1 = 'I\'m inside class A\'s constructor '
        self.spec = 'Special'

class B(A):
    classvar2 = 'I\'m a class variable in class B'
    def __init__(self):
        super().__init__()
        self.var1 = 'I\'m inside class B\'s constructor '
        print(super().classvar1)

a = A()
b = B()
print(b.spec) #This code will not be printed because the constructor of class A has been overrided. If you want to run the constructor of class A along with the constructor of class B then you can use super()
