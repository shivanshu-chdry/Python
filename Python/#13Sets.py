#Set is a collection of well defined objects
s = set()
print(type(s))

s_from_list = set([1, 2, 3, 4, 5])
print(s_from_list)

s.add(1) #To add anything in a set
s.add(2) #Unlike lists 1 will not be returned here one more time because set only return unique values
s.remove(2) #If you want to remove something from your set

s1 = s.union({1, 2, 3, 4}) #It makes a new set

s1 = s.intersection({1, 2}) #It'll return the values which are present in both sets
print(s, s1)

print(s.isdisjoint(s1))