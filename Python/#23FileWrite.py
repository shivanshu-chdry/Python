f = open('#22file1.txt', 'w') #You can even make a new file
f.write('Python is da best ;)')
f.close() 
# if you want to append
a = open('#22file.txt', 'a')
a.write('You can install python from it\'s website') 
a.close()
#Handle Read And Write Both
s = open('#22file2.txt', 'r+') #r+ is used when you want to read and write in the file at the same time
print(s.read())
s.write(' \nthank you!')
s.close()