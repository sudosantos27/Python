import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word: # we itirate until we find a word that does not have a - or a space 
        word = random.choice(words)

    return word.upper() # we return the word but uppercase, we make everything uppercase so there is no problem when choosing


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  
    # we create a set with the letters in the word, would be like this: Python -> {P, y, t, h, o, n}
    alphabet = set(string.ascii_uppercase) # we create a set with all uppercase letters
    used_letters = set()  # what the user has guessed

    lives = 20

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        # joins the letter of the set in a string separated with a space
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters: 
            # alphabet - used_letters creates a set of the letters that have not been used
            used_letters.add(user_letter)
            # if it was not used, is added to the set
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # if the chosen letter is in the set of the word, it is removed from the word set meaning you guessed it 
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()