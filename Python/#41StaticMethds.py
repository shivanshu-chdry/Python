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

enscarr = Employee('Enscarr', 455, 'Head')
daniel = Employee('Daniel', 234, 'Instructor')
tom = Employee.from_dash('Tom-432-Director')
print(tom.printgood('Shivanshu'))