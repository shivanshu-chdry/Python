class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f'Name is {self.name}. Salary is {self.salary} and role is {self.role}'

#You can't enter value in employee. The way to enter value in employee are known as constructors
enscarr = Employee('Enscarr', 455, 'Head')
daniel = Employee('Daniel', 234, 'Instructor')
#Rather than typing like this you can enter the values in employee
# enscarr.name = 'Enscarr'
# enscarr.salary = 455
# enscarr.role = 'Head'

# daniel.name = 'Daniel'
# daniel.salary = 234
# daniel.role = 'Instructor'

print(enscarr.name)
print(daniel.salary)
print(enscarr.printdetails())
