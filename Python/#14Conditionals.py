var = 6
var1 = 56
print('Enter your number')
var2 = int(input())

if var2>var1:
    print('Greater')

elif var2==var1:
    print('Equal') #Elif is used if you want python to skip rest of the ifelse ladder

else:
    print('Lesser')

list = [1, 2, 3, 4, 5]
print(5 in list)
if 5 in list:
    print('Yes, It\'s in the list')

print(5 not in list)
if 65 not in list:
    print('No, It\'s not in the list')
