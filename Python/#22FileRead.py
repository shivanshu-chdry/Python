f = open('#22file.txt', 'rt')
content = f.read()
print(content)
for line in content:
    print(line) #There will be a new line after every character

s = open('#22file.txt')
print(s.readline()) #readline helps in reading the lines

print(s.readlines()) #It'll print everything in a list

f.close() #You should close a file which you have opened