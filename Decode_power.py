# This program helps show the power and speed of a computer. U give it a random number between 0 and whatever range you want and it attempts to guess it.
# Trust me, youll be amazed.
# this is a crazy game where the computer plays against the computer to guess a random number generated by either a computer or a user
# its nice as it reveals the power and speed of your computer... 

import random
import time 

# user to play against computer
def user_vs_comp(number, range_of_input):
    count = 0
    print("\nThe computer has started the attempt to guess your random number... No cheating here!\n")
    computer_guess = random.randint(0, range_of_input)
    start_time = time.time()
    while computer_guess != number:
        count += 1
        computer_guess = random.randint(0, range_of_input)
    if computer_guess == number:
        end_time = time.time()
    #taking the stats
    success_stat = (f'After {count} tries, I managed to decode your number. It was {number}')
    time_taken = end_time - start_time 
    if time_taken > 10:
        status = 'That was tiring and hard! Kudos and try me again!..'
    else:
        status = "That wasn't that hard... Took me less than 10 seconds. :)"
    
    print('-----------------------------------------------------------------------------------')
    print(f"\nThese are the stats:\nStatus: {success_stat}\ntime taken: {time_taken}\n{status}\n")
    print('-----------------------------------------------------------------------------------')

# computer to play against itself
def comp_vs_comp():
    count = 0
    start_time = time.time()
    comp1 = random.randint(0, 10000000)
    print('\nThe computer has chosen a random integer between 0 and 10 million')
    print('The computer will attempt to try and find that number!')
    comp2 = random.randint(0, 10000000)
    while comp2 != comp1:
        comp2 = random.randint(0, 10000000)
        count += 1
    if comp2 == comp1:
        end_time = time.time()
        time_used = end_time - start_time
        print(f'\nDone! After {count} attempts, i found the number! It was {comp1}\nIt took {time_used}')



print("\nDo you want to play against the computer or the computer to play against itself?")
who_to_play = input("answer with ('me' or 'comp'):\n")


if who_to_play == 'me':
    user_guess = int(input('\nEnter a number for the computer to guess, make it hard!\n'))
    range_of_input = int(input('\nWhat range do you give the computer to guess?\n(0-?)'))
    user_vs_comp(user_guess, range_of_input)

elif who_to_play == 'comp':
    comp_vs_comp()
