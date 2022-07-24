import time

#If I wanna see which one is faster then I can do:
initial = time.time() #Time function returns the tick speed
k = 0
while k<45:
    print('I\'m Shivanshu!')
    k = k + 1
print(time.time() - initial) #Will give the speed of while loop

initial2 = time.time()
for i in range(45):
    print('This is Shivanshu!')
print(time.time() - initial2) #Will give the speed of for loop

#local time function
#time function will return the tick speed local time will convert it to the local time which will be a tupple and asctime will convert that tupple in a representable time 
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#Sleep function
a = 0
while a<10:
    print('Sleep Function')
    time.sleep(2) #Now this program will print "Sleep Function" after every 2 seconds
    a = a + 1