#Rock, Paper and Scissors Game
import random

option = ['R', 'P', 'S']
user_points = 0
comp_points = 0
no_of_chances = 0
chances = 10

while (no_of_chances<10):
    user = input('Enter R for Rock \nP for Paper \nS for Scissors\n')
    choice = random.choice(option)
    if user=='R' and choice=='P':
        print('Rock Crushes the Paper. You won this time!')
        user_points = user_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='P' and choice=='P':
        print('It\'s paper everywhere. Tie!')
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='S' and choice=='P':
        print('Scissors cut the Paper. You won this time!')
        user_points = user_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='R' and choice=='R':
        print('You broke my Rock with your Rock. Tie!')
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='P' and choice=='R':
        print('Rock Crushes Paper. You lose this time!')
        comp_points = comp_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='S' and choice=='R':
        print('Rock broke the Scissors. You lose this time!')
        comp_points = comp_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances) 
        no_of_chances = no_of_chances + 1
        
    elif user=='R' and choice=='S':
        print('Rock broke the Scissors. You won this time!')
        user_points = user_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1
        
    elif user=='P' and choice=='S':
        print('Scissors cut the paper. You lose this time!')
        comp_points = comp_points + 1
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)  
        no_of_chances = no_of_chances + 1
        
    elif user=='S' and choice=='S':
        print('Both are Scissors. Tie!')
        print('Your Points:',user_points)
        print('Oponent Points:',comp_points)
        print('Number of Chances left:',9 - no_of_chances)
        no_of_chances = no_of_chances + 1

    elif no_of_chances>chances:
        print('')
print('Your Points:',user_points)
print('Oponent Points:',comp_points)
if user_points>comp_points:
    print('You win!')
elif user_points<comp_points:
    print('You lose!')
elif user_points==comp_points:
    print('Tie!')
print('GAME OVER~')

