#Abstract Base Class And Abstract Methods
from abc import ABCMeta, abstractmethod

class Shape(metaclass = ABCMeta): #You can't make objects of a class where abstractmethod has been used.
    @abstractmethod #You can use abstract methods if you want someone to use them in every class.
    def reactarea(): 
        return 0

class Rectangle:
    type = 'Rectangle'
    sides = 4
    def __init__(self):
        self.length = 10
        self.breadth = 5
    
    def rectarea(self):
        print(f'{self.length * self.breadth}cm2')

a = Rectangle()
a.rectarea()
