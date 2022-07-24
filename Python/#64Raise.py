inp = input('enter your name')
money = input('How much do you earn')

if int(money) == 0:
    raise ZeroDivisionError('The Program is stopped because you\'re salary is 0')
if inp.isnumeric():
    raise Exception('Numbers are not allowed') #This will raise an exception if the input is a number

print(f'Hello {inp}')

c = input('Enter your name')

# try:
#     print(a)

# except Exception as e:
#     if c=='Shivanshu':
#         raise ValueError('Shivanshu is blocked...')

#     print('Exception handled')