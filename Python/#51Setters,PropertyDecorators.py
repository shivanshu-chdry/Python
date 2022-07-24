class Employee:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        # self.email = f'{name1}.{name2}@gmail.com'
    
    def explain(self):
        return f'The Employee is {self.name1} {self.name2}'
    #Now if you want to use this function as an attribute you can use @property which is a decorator
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

shekhar = Employee('Shekhar', 'Malik')
shivanshu = Employee('Shivanshu', 'Chaudhary')

print(shekhar.explain())
#print(shekhar.email())

#Now if you want to change the first name you can do it like this:
shekhar.name1 = 'SHEKHAR'
print(shekhar.explain())
#print(shekhar.email()) #Now here you can see that the email is not changed in this condition you can (visit line 10)

print(shekhar.email)
shivanshu.email = 'shivanshu.chaudhary'
shivanshu.email = 'shivanshu.chaudhary@gmail.com' #This is not throwing error because there is an function to set this (line 14)

#Now if you want to delete shivanshu.email
del shivanshu.email #This will throw error because there is no deleter present so we can make one (line 20)
print(shivanshu.email) #Now it'll return none.none@gmail.com if you don't want it to return this visit(line 12)
