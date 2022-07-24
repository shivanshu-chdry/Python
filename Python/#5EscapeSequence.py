#Escape Sequences
print('C:\ahivanshu') 
# It'll not print C:\ashivanshu because it'll complete /a first because they are the escape sequence character.
# Names of escape sequence characters:
# \n - New line
# \t - Leaves the space of a tab
# \' - Gives single quote
# \" - Gives double quote
# \\ - Gives Backslash
# \r - Carriage Return
# \b - Backspace
# \f - Formfeed
# \0 - Null Character
# \N{Name} - Unicode character Database named lookup
# \uxxxxxxxx - Unicode character with a 16-bit hex value
# \Uxxxxxxxx - Unicode character with a 32-bit hex value
# \000 - Character with octal value ooo
# \xhh - Character with hex value hh
print('C:\\ahivanshu')
print('C:\'ahivanshu') #To type C:'ahivanshu
print('C:\"ahivanshu') #To type C:"ahivanshu
print('Shivanshu is a \n smart boy \t1')
print("Shivanshu \' good boy")