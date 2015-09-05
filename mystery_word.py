import random
#from sys import exit


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_word_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <=6:
            easy_word_list.append(word)
    return easy_word_list


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <=8:
            medium_word_list.append(word)
    return medium_word_list


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return word_list[random.randint(0,len(word_list))].lower()


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # Have a collector list, insert upper() of iteration variable if present
    # insert '_' if not in word
    display = []

    for char in word:
        if char in guesses:
            display.append(char.upper())
        else:
            display.append('_')
    return ' '.join(display)


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    is_complete = True
    # guess_string = ''.join(guesses)
    for char in word:
        if char not in guesses:
            is_complete = False
    return is_complete


def user_guess(guesses):
    # user_guess = ''
    while True:
        user_guess = input("\n"+"-"*55+"\nPlease guess a letter.\n> ").lower()
        if len(user_guess) == 0:
            continue
        elif len(user_guess) > 1:
            print("Please enter one letter at a time.")
            continue
        elif not user_guess.isalpha():
            print("Please enter letters only.")
            continue
        else:
            # Don't allow already guessed letters
            if user_guess in guesses:
                print("You have already guessed "
                      "\'{}\'.".format(user_guess.upper()))
                continue
            break
    return user_guess


def user_continue():
    user_continue = ''
    continue_bool = False
    while True:
        user_continue = input("Play again? [Y]/[n]: ").lower()
        if user_continue == '' or user_continue == 'y':
            continue_bool = True
            break
        elif user_continue == 'n':
            continue_bool = False
            print("\nHave a nice day!".upper())
            break
        else:
            continue
    return continue_bool


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    word_list = []          # holds entire dictionary
    game_word = ''          # holds random word from specified game mode
    guessed_letters = []    # holds letters guessed by the user
    temp_guess = ''         # temp variable to hold user input in MAIN GAME LOOP
    allowed_guesses = 1     # number of guesses allotted to user per game (8)
    num_guesses = 0         # number of expended user guesses
    play_again = False      # records whether player wants to play again

    # Read in entire dictionary
    with open('/usr/share/dict/words') as f:
        word_list = f.read().split()

    print("\n"+('#'*10+"    Welcome to Mystery Word!    "+'#'*10).upper().center(55)+"\n")

    '''
    I'm considering wrapping all of the below in a while loop because only code
    within main() is run when called; no way to use a sentinel defined outside
    What would drive this loop? It has to run every time; while True
    '''

    # User game mode input
    while True:
        print("\nPlease select your level of difficulty (press Q to quit):")
        difficulty_level = input( "[E]asy, [M]edium, or [H]ard.)\n> ").lower()
        if difficulty_level == 'e':
            game_word = random_word(easy_words(word_list))
            break
        elif difficulty_level == 'm':
            game_word = random_word(medium_words(word_list))
            break
        elif difficulty_level == 'h':
            game_word = random_word(hard_words(word_list))
            break
        elif difficulty_level == 'q':
            break
        else:
            print("\nInvalid selection.")
            continue

    # MAIN GAME LOOP
    while len(game_word) != 0 and num_guesses < 8:
        # Print current state of word with underscores for unguessed letters
        print(display_word(game_word, guessed_letters).center(55))
        print("Test: {}".format(game_word)) # TEST TO REMOVE
        print("\nYou have {} guesses remaining.".format(allowed_guesses - num_guesses))

        # Get guess from user and add to guessed_letters list
        guessed_letters.append(user_guess(guessed_letters))

        # Add to guess tally if letter is not in game_word
        if guessed_letters[-1] not in game_word:
            num_guesses += 1

        # Show guessed letters
        print("\nLetters already guessed:\n"+', '.join(guessed_letters).upper())

        if is_word_complete(game_word, guessed_letters):
            print(display_word(game_word, guessed_letters).center(55))
            print("\nYou win!".upper())
        elif num_guesses >= allowed_guesses:
            print("\nYou have run out of guesses.".upper())
            print("\n\nThe word you were trying to guess was: {}".format(game_word.upper()))


        #TODO
        # Game clean-up; this needs to be outside of game loop
        if is_word_complete(game_word, guessed_letters) or num_guesses >= allowed_guesses:
            play_again = user_continue()
            if play_again:
                game_start = False
                continue
            else:
                break

    # print(is_word_complete(game_word, list(guessed_letters)))
    # print(display_word(game_word, list('abcdefg')).center(55))


if __name__ == '__main__':
    main()
