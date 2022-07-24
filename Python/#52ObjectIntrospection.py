#Object Introspection means to get information about an object
class Employee:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    
    def explain(self):
        return f'The Employee is {self.name1} {self.name2}'
    
    @property
    def email(self):
        if self.name1 == None or self.name2 == None:
            return 'Email does not exist!'
        return f'{self.name1}.{self.name2}@gmail.com'

    @email.setter
    def email(self, str):
        names = str.split('@')[0]
        self.name1 = names.split('.')[0]
        self.name2 = names.split('.')[1]

    @email.deleter
    def email(self):
        self.name1 = None
        self.name2 = None

elonmusk = Employee('Elon', 'Musk')

print(type(elonmusk)) #It tells us about the type
print(id(elonmusk)) #It will print the id(a unique number assigned to every object)
print(dir(elonmusk)) #This will give all the functions of elonmusk

#Inspect function
import inspect
print(inspect.getmembers(elonmusk))
