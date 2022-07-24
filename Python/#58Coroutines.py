#If you want to run a function from between you can use coroutines
def searcher():
    import time
    book = 'This is a random text for better understanding of coroutines'
    time.sleep(4)

    while True:
        text = (yield) #Here I'm telling my interpreter that this is a coroutine
        if text in book:
            print('This text is in the book')
        else:
            print('This text is not in the book')

search = searcher()
print('Process Started...')
next(search) 
search.send('of coroutines')
print('Next Method run')
search.send('is not')

search.close() #You can also close the coroutines like files
