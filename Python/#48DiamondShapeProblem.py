#Diamond Shape Problem create confusion that which method from which class has to be implemented.

class A:
    def met(self):
        print('This is a method of class A')

class B(A):
    def met(self):
        print('This is a method of class B')

class C(A):
    pass

class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met() #Here function of class B will be implemented first.