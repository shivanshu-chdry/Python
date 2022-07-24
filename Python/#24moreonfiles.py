f = open('#22file.txt')
# print(f.tell()) #Tell the character where it has reached
print(f.readline())
f.seek(0) #This will reset the pointer and the first line will be printed again
# print(f.tell())
print(f.readline())
# print(f.tell())
f.close()