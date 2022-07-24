with open('#22file.txt') as f:
    a = f.readlines()
    print(a)
# No need to close the file here because the with block will automatically close it
