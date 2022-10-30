import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
   
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'You have {lives} lives left and you have used', ' '.join(used_letters))

        # what current word is eg W-RD
        word_list = [letter if letter in used_letters else '-' for letter in word] # prints the letter both in word # and used letters else -
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: \n').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print('Letter not in word')
        
        elif user_letter in used_letters:
            print(f'\nYou have already guessed {user_letter}. Try another!\n')

        else:
            print('\nYou entered an invalid character\n')

    # exits when they have won or lives == 0
    if lives == 0:
        print(f'\nLives over. Sorry! The answer was {word}...\n')
        c_or_stop = input('Would you like to continue with the game (y/n)?')
        if c_or_stop == 'y':
            hangman()
        else:
            print('Thanks for playing')
    else:
        print('\nYou won! Congrats...\n')

hangman()
