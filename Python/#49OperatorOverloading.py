#Operator Overloading And Dunder Methods

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary #You can override any operator like this

    def __truediv__(self, other):
        return 78

emp1 = Employee('Tom', 555, 'Programmer')
emp2 = Employee('Jerry', 78, 'Cleaner')
print(emp1 + emp2)
print(emp1 / emp2)
