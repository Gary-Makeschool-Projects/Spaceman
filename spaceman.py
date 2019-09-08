import random
from bisect import bisect_left
import pyfiglet
import os
from colorama import Fore


def userInput():
    '''
      @Description:
            A function that returns a string given by user
      @Returns:
            str: anything the user enters
      '''
    x = input('>> ')
    return x


def validInput(var):
    '''
    @Description:
        A function that checks if a given string is in the alphabet and has to be a single character from the list.
    @Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    if var.isalpha() and len(var) > 0 and len(var) < 2:
        return True
    else:
        return False


def load_word():
    '''
    @Description: A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    @Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    with open('words.txt', 'r') as f:
        # open the file in read mode
        words_list = f.read().split(' ')  # open the file in read
    # get a random word from the file
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    @Description:
        A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    @Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    @Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # matches = []
    # # nice one liner I tried implementing but only stores a single match :(
    # found = [letter for letter in secret_word if letter in letters_guessed]
    # matches.append(found[0])
    word = []  # temporary array of matches
    for letters in secret_word:
        if letters in letters_guessed:
            word.append(letters)  # add matches to word[]
        else:
            # bind underscores to hide the rest of the secret word
            word.append('_')
    return ''.join(word)


def is_guess_in_word(guess, secret_word):
    '''
      @Description:
            A function to check if the guessed letter is in the secret word
      @Args:
            guess (string): The letter the player guessed this round
            secret_word (string): The secret word
      @Returns:
            bool: True if the guess is in the secret_word, False otherwise
      '''
    for letter in secret_word:
        if letter == guess:
            return True

    return False

# Search algorithm for sinister spaceman


# def search(currentword):

#     with open('words.txt', 'r') as f:
#         wordlist = f.read().split(' ')
#     # the left enpoint

#     related = []  # related results
#     l = 0  # left endpoint
#     r = len(wordlist)  # right endpoint
#     m = l + ((r - l) // 2)  # midpoint
#     key = len(currentword)
#     found = bisect_left(wordlist, key, index)
#     if len(wordlist[index]) == val:
#         related.append(wordlist[index])

#     # while the left endpoint is less than or equal to the right enpoint we are going to keep searching
#     while (l <= r):
#         m = l + ((r - l) // 2)  # midpoint
#         size = (currentlen == len(wordlist[m]))
#         # Check if value is present at mid
#         if (size == 0):
#             return m - 1

#         # If value greater, ignore left half
#         if (size > 0):
#             l = m + 1

#         # If x is smaller, ignore right half
#         else:
#             r = m - 1

#     return -1
def test(): pass
# just a test fucntion nothing to see here


def play_again():
    '''
    @Description:
        A function that is used to determine if the user wants to continue playing spaceman
    @Returns:
        bool: return True if user enters yes return False if user enters no otherwise return not an option
    '''
    print('===============================================')
    print('Would you like to play again?')
    answer = input(">> ")
    if answer == 'yes':
        os.system('clear')
        return True
    elif answer == 'no':
        os.system('clear')
        return False
    else:
        print('[-] Not an option')
        return True


def banner():
    with open('fonts.txt', 'r') as f:
        # open the file in read mode
        kind = f.read().split('\n')
    # get a random word from the file
        spaceman = random.choice(kind)
    print(Fore.LIGHTBLUE_EX +
          pyfiglet.figlet_format('Spaceman', font=spaceman) + Fore.RESET)


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    guess_ammount = len(secret_word)  # guess limit
    correct = []  # correct guesses
    unused = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z']  # unused letters

    # create banner
    banner()

    while True:

        if guess_ammount == 0:
            print(Fore.RED + "You lost :(")
            print(
                "The word was: {}".format(secret_word) + Fore.RESET)
            break

        if is_word_guessed(secret_word, correct):
            print("You won!")
            break

        print('Enter a letter: ')
        letter = userInput()

        if validInput(letter):
            if letter not in unused:
                print("You already entered: " + letter)
                continue

            unused.remove(letter)
            remaining = ','.join(unused)

            if is_guess_in_word(letter, secret_word):

                correct.append(letter)
                print(Fore.LIGHTGREEN_EX +
                      "[+] " + letter + " is in the word!" + Fore.RESET)
                print(get_guessed_word(secret_word, correct))
            else:
                guessed_word = get_guessed_word(secret_word, correct)

                guess_ammount -= 1

                print(Fore.RED + "[-] Incorrect: " +
                      letter + " not in the word")
                print("You have {} incorrect guesses left".format(
                    guess_ammount))
                print("Guessed word so far: {}".format(guessed_word))
                print("Letters you haven't guessed:  {}".format(
                    remaining) + Fore.RESET)


run = True
while run:
    spaceman(load_word())
    run = play_again()
print('[-] Exiting ...')
