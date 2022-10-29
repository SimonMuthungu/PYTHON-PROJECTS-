# In rock this rock paper scissors game, youll give your choice to compete against the computers choice. Either of you have an equal chance of winning. Good luck!!
import random

# let the computer choose between the three options
choices = ['r', 'p', 's']
rps = random.choice(choices)

#Taking the users name
User_name = input('Please enter your name...: \n')
print('--------------------------------------')
print(f'\nWelcome to the game, {User_name}. In this game, you\'ll compete with me, Simon!')
print('Lets begin...')
print('--------------------------------------')

# both users and computer start with 10 points
user_stars = 10
computer_stars = 10
count = 0 # count number of tries

guess_list = ['r', 'p', 's'] # to ensure user's select one of r, p and c

while True:
    user_guess = input(f'\nenter your guess, {User_name}... r-(rock), p-(paper) or s-(scissors), q-quit game!. Both of us are at 10 points!!\n').lower()

    if user_guess == 'q': 
        print(f'Thank you for playing our game, {User_name}. See you next time... \n') #quits the game and breaks out!
        break

    elif user_guess in guess_list:
        if user_guess == rps: # there might be a tie which doesn't count

            count += 1
            print(f'We tied!! We both chose {rps}')
            rps = random.choice(choices)
        
        #checks whether user is the winner or else computer and assigns the necessary scores and picks a new guess
        elif (user_guess == 'r' and rps == 's') or (user_guess == 'p' and rps == 'r') or (user_guess == 's' and rps == 'p'):
            user_stars += 5
            computer_stars -= 5
            count += 1
            print('-------------------------------------------------------------')
            print(f'Genius! Your stars increased to {user_stars} and my stars decreased to {computer_stars} bcoz I chose {rps}')
            rps = random.choice(choices)

        #where user gets beaten by computer
        else:
            user_stars -= 5
            computer_stars += 5
            count += 1
            if user_stars > 5:
                print('--------------------------------------------------------------------')
                print(f'Nop! {user_guess} cannot beat {rps}! You have {user_stars} stars left ! I am at {computer_stars}\n')
                rps = random.choice(choices)

            # Just to warn the user of their last chance
            elif user_stars == 5:
                print(f'\nNop! {user_guess} cannot beat {rps}! {user_stars} stars left! I have {computer_stars} stars...\n')
                print(f'Danger, one more fail and youre out.\n')
                rps = random.choice(choices)

            else:
                print(f'you have {user_stars} stars left and I have {computer_stars} stars left :)')
                rps = random.choice(choices) 
            
    else: # choice not r, p or s
        print('try again, make a correct selection this time - Either r-(rock) or p-(paper) or s-(scissors)')
        count += 1


# congratulating the winner, they deserved it!
print('Winning Stats: \n')
print('Player 1: Simon', f'Player 2 {User_name}\n')
print('Number of tries: ', count, '\n')
print(f'Player 1 score: {computer_stars}.')
print(f'Player 2 score: {user_stars}.\n')

if computer_stars > user_stars:
    print('---------------------------------------------------------')
    print(f'Simon has won!! I had {computer_stars} while you had {user_stars}.\n')
else:
    print('---------------------------------------------------------')
    print(f'{User_name} Won!! You have {user_stars} while I have {computer_stars}')