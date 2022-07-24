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

class Player:
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f'Name is {self.name} and game is {self.game}'

class CoolProgrammer(Employee, Player):
    language = 'C++'
    def printlang(self):
        print(self.language)

enscarr = Employee('Enscarr', 455, 'Head')
daniel = Employee('Daniel', 234, 'Instructor')

sam = Player('Sam','Baseball')
frais = CoolProgrammer('Frais', '100000', 'CoolProgrammer')
frais.printlang()
