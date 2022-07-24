#Break And Continue Statements
i = 0
while (True): #While true loop never stops
    if i+1<5:
        i = i + 1
        continue #Continue statement will not allow the program to come down until the above condition becomes false
    print(i)
    if i==44:
        break #Stop the loop
    i = i + 1
