#Public, Private and Protected Access Specifiers

class Employee:
    no_of_leaves = 8
    public = 8       #Public variables can be used anywhere.
    _protec = 9      #Protected variables can only be used by the class and other instances of the class. However, It can't be used by any other class
    __private = 10   #Private variables cannot be used outside the class it can only be used inside the class.

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        lst = string.split('-')
        return cls(lst[0], lst[1], lst[2])

    @staticmethod
    def printgood(string):
        print('This is good ' + string)

navya = Employee('Navya', 333, 'Student')
print(navya._protec)
print(navya._Employee__private)#private variables can be accessed by typing _[class name]__[variable name]
