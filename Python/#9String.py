str = "shivanshu is a good boy"
print(str[3]) #Python index starts from 0
print(str[0:10])#You need to write one extra digit cause here 11 is included but 20 is excluded that's why it's showing results from 11 to 19
print(len(str))#len is a function for knowing the length 
print(str[0:10:2])
print(str[:10])#It'll automatically take 0
print(str[0:])#It'll automatically take the length of str
print(str[0:10:])#It'll automatically take 1
#Negative Index
print(str[-5:-1]) #We can take start taking numbers from the back which will start from -1
print(str[::-1]) #The string will be reversed
print(str[::-2])
#Some Important String Functions:
print(str.isalnum()) #This will show a boolean character which is false because str is not alpha numeric
str1 = "Shivanshuisagoodboy"
print(str1.isalnum()) #The result is true because there are no spaces in the string


print(str.isalpha()) #This function gives result after checking whether the number is alpha and numeric or not

print(str.endswith('boy')) #It's true because str is ending with boy
print(str.endswith('good')) #It's false because str is not ending with good

print(str.count("s")) #This will count the number of s in str 

print(str.capitalize()) #This function will capitalize the first letter of str

print(str.find('is')) #This helps you in finding a word if the string is too long

print(str.lower()) #This will change all the letters in str to lower case
print(str.upper()) #This will change all the letters in str to upper case

print(str.replace('shivanshu', 'shekhar'))