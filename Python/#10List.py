grocery = ['Lays', 'Soap', 'Vegetables', 'Fruits', 'Milk', 20, 25.48] #A List can contain Strings, int and float
print(grocery)
print(grocery[0])
numbers = [2, 8, 45, 85, 21, 3]
numbers.sort() #Ascending order Function
print(numbers)
print(numbers[2])
numbers.reverse() #Descending order Function
print(numbers) 
print(numbers[2])
#List Slicing 
print(grocery[2:4]) #It'll show results till 3 if you type 4
print(grocery[2:7])
num1 = [2, 5, 85, 21, 45, 12]
print(num1[0:5:1]) #By Default Values
print(num1[::2])
print(num1[::-1]) #The list will be reversed
print(num1[::-2])
print(num1[1:5:-3])

list = [5, 8, 685, 7, 354, 752]
#Some Important List Functions

print(len(list)) #Used for knowing the length of the list

print(max(list)) #Used for knowing the maximum number in the list

print(min(list)) #Used for knowing the minimum number in the list

list.append(52) #This can be used to add something at the last in a list
print(list)

list.insert(3, 666) #This function can be used if you wanna add something in between the list
print(list)

list.remove(8) #This function can be used if you wanna remove something from the list
print(list)

list.pop() #It'll remove the last number from the list
print(list)