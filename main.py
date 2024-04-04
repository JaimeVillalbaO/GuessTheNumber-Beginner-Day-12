import random
from acsi_day12 import logo
import os 

game_over = False
while game_over == False:

    os.system('cls') 
    print(logo)
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')

    number = random.randint(1, 100)    
    attemps_easy = 10
    attemps_hard = 5    

    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    while not game_over :
        if difficulty == 'easy':  
            print(f'You have {attemps_easy} attemps remmaining to guess the number. ')
            option = int(input('Make a guess: '))
            if option == number:
                print(f'You got it. The answer was {number}')
                game_over = True
            elif option > number:
                print('Too high')
            else:
                print('Too low')
            attemps_easy -= 1
            if attemps_easy == 0:
                print('You\'ve run out of guesses. You losed ...')
                game_over== True
        else:
            print(f'You have {attemps_hard} attemps remmaining to guess the number. ')
            option = int(input('Make a guess: '))
            if option == number:
                print(f'You got it. The answer was {number}')
                game_over = True
            elif option > number:
                print('Too high')
            else:
                print('Too low')
            attemps_hard -= 1
            if attemps_hard == 0:
                print(f'You\'ve run out of guesses. You losed... the number was {number}')
                game_over = True



    if game_over == True:
        again = input('Do you  want to play again. Write "y" to play again, "n" to finish. ')
        if again == 'y':
            game_over = False
        else:
            game_over = True
        