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


enscarr = Employee('Enscarr', 455, 'Head')
daniel = Employee('Daniel', 234, 'Instructor')


Employee.change_leaves(90)

print(Employee.no_of_leaves)
