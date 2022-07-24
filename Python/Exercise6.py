#Make a program which takes user input until the user enter a number greater than 100
while (True):
    num = input('Enter a number:')
    if int(num)>100:
        print('Congratulations, you gave a number greater than 100')
        break
    else:
        print('Try again!')
        continue