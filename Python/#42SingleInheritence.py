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

    @classmethod
    def from_dash(cls, string):
        lst = string.split('-')
        return cls(lst[0], lst[1], lst[2])

    @staticmethod
    def printgood(string):
        print('This is good ' + string)

class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f'Programmer\'s name is {self.name}. Salary is {self.salary}, role is {self.role} and languages are {self.languages}'

enscarr = Employee('Enscarr', 455, 'Head')
daniel = Employee('Daniel', 234, 'Instructor')

shagun = Programmer('Shagun',321, 'Programmer', 'Python')
shekhar = Programmer('Shekhar', 330, 'Programmer', 'Python and C++')
print(shekhar.printprog())
