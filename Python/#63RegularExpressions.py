import re

mystr = '''New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean.
At its core is Manhattan, a densely populated borough that\'s among the world\'s major commercial, 
financial and cultural centers.'''

#Primarily some functions in regular expressions are:
#findall, finditer, search, split, sub
patt = re.compile(r'New York') #This can give the matches from the str
#To know about meta and special sequences visit '#63RE.txt'. They can be used like this:
print('Meta Characters')
patt1 = re.compile(r'^New York') #The string starts with New York that's why it's giving me the match
patt2 = re.compile(r'New York$')#This will not return anything as the string doesn't start with New York
matches = patt.finditer(mystr)

print('Special Sequences')
patt3 = re.compile(r'\A Georgia') #/A will tell whether the word is in the beginning of the sentence or not
patt4 = re.compile(r'\b centers.') #Return the match if the character is at the beginning or at the end
patt5 = re.compile(r'centers.\b')

for match in matches:
    print(match)

print(mystr[0:8]) #The matches can be printed like this

#Task:
#Find phone numbers starting from +91 in a str
numbers = 'Numbers are: +91 4567891230 +91 1754982467 +91 4567891234'
patt = re.compile(r'.+91 \d{10}')
matches = patt.finditer(numbers)
for match in matches:
    print(match)
