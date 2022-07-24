#Health Management System


print('Welcome to Health Management System!')

def gettime():
    import datetime
    return datetime.datetime.now()

lr = int(input('Enter 1 for log \n2 for retrieve\n'))

def retrieve():
    client = int(input('Enter 1 for Shivanshu \n2 for Navya \n3 for Shekhar\n'))
    if client==1:
        if lr==2:
            print('What do you want to retrieve for Shivanshu?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))
                
        if choice==1:
            s = open('Exercise9Shivanshufood.txt', 'r')
            print(s.readlines())
            s.close()

        elif choice==2:
            s = open('Exercise9Shivanshuex.txt', 'r')
            print(s.readlines())
            s.close()

    elif client==2:
        if lr==2:
            print('What do you want to retrieve for Navya?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))
                
        if choice==1:
            s = open('Exercise9Navyafood.txt', 'r')
            print(s.readlines())
            s.close()
        
        elif choice==2:
            s = open('Exercise9Navyaex.txt', 'r')
            print(s.readlines())
            s.close()

    elif client==3:
        if lr==2:
            print('What do you want to retrieve for Shekhar?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))
                
        if choice==1:
            s = open('Exercise9Shekharfood.txt', 'r')
            print(s.readlines())
            s.close()
        
        elif choice==2:
            s = open('Exercise9Shekharex.txt', 'r')
            print(s.readlines())
            s.close()
    


def log():
    client = int(input('Enter 1 for Shivanshu \n2 for Navya \n3 for Shekhar\n'))

    if client==1:
        if lr==1:
            print('What do you want to log for Shivanshu?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))
        if choice==1:
            f = open('Exercise9Shivanshufood.txt', 'a')
            data = input('Enter what Shivanshu has eaten\n')
            print('Successfully Registered!')
            f.write(str([str(gettime())]) + ' ' + data + "\n")
            f.close()

        elif choice==2:
            f1 = open('Exercise9Shivanshuex.txt', 'a')
            data = input('Enter what Exercise Shivanshu has done\n')
            print('Successfully Registered!')
            f1.write(str([str(gettime())]) + ' ' + data + '\n')
            f1.close()

    elif client==2:
        if lr==1:
            print('What do you want to log for Navya?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))

        if choice==1:
            f2 = open('Exercise9Navyafood.txt', 'a')
            data = input('Enter what Navya has eaten\n')
            print('Successfully Registered!')
            f2.write(str([str(gettime())]) + ' ' + data + "\n")
            f2.close()

        elif choice==2:
            f3 = open('Exercise9Navyaex.txt', 'a')
            data = input('Enter what Exercise Navya has done\n')
            print('Successfully Registered!')
            f3.write(str([str(gettime())]) + ' ' + data + '\n')
            f3.close()

    elif client==3:
        if lr==1:
            print('What do you want to log for Shekhar?')
            choice = int(input('Enter 1 for Diet \n2 for Exercise\n'))

        if choice==1:
            f4 = open('Exercise9Shekharfood.txt', 'a')
            data = input('Enter what Shekhar has eaten\n')
            print('Successfully Registered!')
            f4.write(str([str(gettime())]) + ' ' + data + "\n")
            f4.close()

        elif choice==2:
            f5 = open('Exercise9Shekharex.txt', 'a')
            data = input('Enter what Exercise Shekhar has done\n')
            print('Successfully Registered!')
            f5.write(str([str(gettime())]) + ' ' + data + '\n')
            f5.close()

if lr==2:
    retrieve()
if lr==1:
    log()
