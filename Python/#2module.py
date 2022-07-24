#To install Modules type $pip install[module name]. Pip is the package manager of python. It extract modules from the Internet
#You should not make a file with the name of a module
import random  # These are known as built-in modules of python
#import tensorflow  # This is an external module
import time
#random
random_number = random.randint(0, 5) #Gives you a random integer
print(random_number)

rand = random.random() * 100 #It generates numbers from 0 to 1 if you want to get a random number from 0 to 100 you can multiply it by 100
print(rand)

lst = ['Shivanshu', 'Navya', 'Shekhar', 'Shagun']
choice = random.choice(lst) #Will give a random name from lst
print(choice)
#For more functions you can visit the official documentation of random module
