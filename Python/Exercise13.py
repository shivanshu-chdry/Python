#Pickle iris.data file and read it 
import pickle
with open ('Exercise13iris.txt') as f:
    data = f.read().splitlines()
#Pickling
with open('Exercise13iris.pkl', 'wb') as fileobj:
    pickle.dump(data, fileobj)

#Reading File
with open('Exercise13iris.pkl', 'rb') as fileobj1:
    read = pickle.load(fileobj1)
print(read)
