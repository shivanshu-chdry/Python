#Make a guess game which have a limited chances of guesses
print('Guess the number between 0 and 30')
print('You have only five chances')
num = 18
ch = 0
while(ch<6):
    en = int(input('Enter your guess:\n'))
    ch = ch + 1
    if en>num:
         print('Enter a lesser number')
    elif en<num:
        print('Enter a greater number')
    if en==num:
        print('You won!')
        break
    if ch==5:
        print('You lose!')
        break