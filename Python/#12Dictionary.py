#Dictionary is key value pairs where key means words and value means meaning
dic = {}
print(type(dic))

dict = {'Shivanshu':'Chicken', 'Shekhar':'Mutton', 'Navya':'Cheese Burger', 'Shagun':'Pizza', 'Shaily':{'B':'Eggs', 'L':'Doughnuts', 'D':'Burger'}}
dict['Ashok'] = 'Bread'
dict['Priyanka'] = 'Sting' 
del dict['Priyanka'] #If you want to delete something from your dictionary
print(dict)
print(dict['Shivanshu'])
print(dict['Shaily'] ['B'])

#Some Important Functions Of Dictioinary:
d3 = dict.copy()
del d3['Navya']
print(dict)
d3 = dict
del d3['Navya']
print(dict) #To avoid this you can do the above thing 

print(dict.get('Shivanshu')) #Will give the value of Shivanshu

dict.update({'Priyanka':'Sting'}) #It'll will add Priyanka in the dict
print(dict)

print(dict.keys()) #Will print all the keys in dict

print(dict.items()) #Will print all the key value pairs