#Else & Finally in Try Except
#We've already learnt about Try And Except. Now, Let's talk about else and finally
f1 = open('#22file.txt')
try:
    f = open('mars.txt') #This file does not exist. And, It'll not throw the error because I've used try except.
#Now if I want to close both the files anyway. Then I can use finally

# except Exception as e:
#     print(e)

except EOFError as e:
    print('This is EOFError', e)

except IOError as e:
    print('This is IOError', e)
#We can also use different type of except statements

else:
    print('Else runs only when except is not running.') #If I create mars.txt file then except will not run and else will be printed

finally:
    print('Run this anyway.')
    #f.close() #This will throw error because we've asked to close f anyway. And, it does not exist.
    f1.close()
