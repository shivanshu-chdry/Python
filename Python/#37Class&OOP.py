'''
Classes - Template
Object - Instance of the class
'''

class Student:
    pass

kathyrn = Student()
shivanshu = Student()
tom = Student()

kathyrn.name = 'Kathyrn'
shivanshu.std = 8
tom.section = 'C'

print(kathyrn.name, shivanshu.std, tom.section)

class Employee:
    no_of_leaves = 8 #This no_of_leaves is for every employee or every object of this class
    pass

enscarr = Employee()
daniel = Employee()

enscarr.name = 'Enscarr'
enscarr.salary = 455
enscarr.role = 'Head'

daniel.name = 'Daniel'
daniel.salary = 234
daniel.role = 'Instructor'

print(Employee.no_of_leaves)
daniel.no_of_leaves = 9 #This will change the value of leaves for daniel only
print(daniel.no_of_leaves)
print(daniel.__dict__) #This will give out the dictionary for daniel
Employee.no_of_leaves = 18 #This will change the value of leaves for everyone object in the class. However, the value of daniel will not be changed
print(enscarr.no_of_leaves)
