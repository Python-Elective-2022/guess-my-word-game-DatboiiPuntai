
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------


# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Creates a set of letters that make up sekrit word
    secret_letters = set([x for x in secret_word])

    # checks if subset and returns
    return secret_letters.issubset(set(letters_guessed))


# Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    secret_list = list(secret_word)

    # checks if each letter has not been guessed and replaces with _
    for i, c in enumerate(secret_list):
        if c not in letters_guessed:
            secret_list[i] = '_'

    return ' '.join(secret_list)


# Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # make a list copy of abc
    abcList = list(abc)

    for l in letters_guessed:
        abcList.remove(l)

    return ''.join(abcList)


# Testcases
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )

def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numGuesses = 8
    letters_guessed = []

    print(f"I'm thinking of a word with {len(secret_word)} letters.")

    while numGuesses > 0:
        print(f"You have {numGuesses} guesses remaining.")
        print(f"Letters available: {get_available_letters(letters_guessed)}")

        guess = input("Guess a letter: ").lower()

        # filter out invalid guesses
        if not guess.isalpha():
            print("Bruh that's not even a letter:", end=" ")
        elif len(guess) > 1:
            print("That's too many letters!:", end=" ")
        elif guess in letters_guessed:
            print("You've already guessed this letter:", end=" ")

        else:
            # when a valid guess is given, append to the letters guessed list
            letters_guessed.append(guess)

            if guess in secret_word:
                print("Correct!:", end=" ")
            else:
                # reduce numGuesses by 1 if incorrect
                print("Incorrect!:", end=" ")
                numGuesses -= 1
        print(get_guessed_word(secret_word, letters_guessed) + '\n')

        # checks win condition
        if is_word_guessed(secret_word, letters_guessed):
            print('You win!')
            break
    # if player runs out of guesses and leaves while loop
    if numGuesses < 1:
        print('You Lose!')
        print(f'The word was {secret_word}.')


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()
