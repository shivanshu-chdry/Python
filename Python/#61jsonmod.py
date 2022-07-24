import json

data = '{"var1":"Shivanshu", "var2":56}'
parsed = json.loads(data) #loads function will parse
print(parsed['var1']) #It makes the dictionary

data2 = {
    'channel_name':'BBC News',
    'cars':['Mercedes','Lamborghini', 'BMW'],
    'food':('Chicken', 'Pizza'),
    'isbad':False #If we run it in our webbrowser console then it'll throw error because in JavaScript False is in lowercase. To make it JavaScript compatible we use json.dumps.
}
jscomp = json.dumps(data2)
print(jscomp)
