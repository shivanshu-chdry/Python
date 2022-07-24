import os

print(os.getcwd()) #This can give us the current working directory
# You can also change your directory which is useful when you're working on a project and want to use some files
# which are not in your directory
# os.chdir('C://')
# print(os.getcwd())
print(os.listdir()) #This will give me all the files of this directory
print(os.listdir('C://')) #This will print all the files in C://

# os.mkdir('Folder1') #mkdir is used to create folder
# os.makedirs('Folder1/Folder2') #This will make Folder1 and then It'll make Folder2 inside Folder1
# os.rename('File1.txt', 'File2.txt') #This will rename the file. Here I've changed File1.txt to File2.txt
print(os.environ.get('Path')) #This will give the enviornment variables
# print(os.path.join('C:/', '#22file.txt'))#This function is used to join two paths

# print(os.path.exists('C://Shivanshu')) #This will return True if the directory exists and false if it does not exist
# print(os.path.isfile('C://Shivanshu')) #This will return True if the file exists and false if it does not exist