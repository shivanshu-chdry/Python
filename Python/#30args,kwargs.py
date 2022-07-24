# *args and **kwargs
#A normal argument can also be passed with *args but it should be written before args
#The order should be [{any normal argument(optional), *args, **kwargs}]
def funargs(normal, *args, **kwargs): #It is not necessary to write it as *args or **kwargs you can also write *tom and **mike or anything you want
    print(normal)
    for item in args:
        print(item) #You can also run the for loop 
    
    for key,value in kwargs.items():
        print(f'{key} is a {value}')

normal = 'I\'m normal and the studets are:'
name = ['Shivanshu', 'Sarthak', 'Ojas', 'Prabhat', 'Madhav'] #Will go as a tupple
kw = {'Shivanshu':'Head Boy', 'Sarthak':'Sports Captain', 'Ojas':'Prefect', 'Madhav':'Student', 'Prabhat':'PTI'}
funargs(normal, *name, **kw)
