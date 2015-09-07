import random
from os import get_terminal_size


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


def display_word(game_word, guessed_letters):
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

    for char in game_word:
        if char in guessed_letters:
            display.append(char.upper())
        else:
            display.append('_')
    return ' '.join(display)


def show_guessed_letters(guessed_letters):
    VOWELS = 'aeiou'
    vowels = []
    consonants = []
    for char in guessed_letters:
        if char in VOWELS:
            vowels.append(char)
        else:
            consonants.append(char)

    print('\n')
    if len(vowels) > 0:
        print('Guessed Vowels:     {}'.format(' '.join(sorted(vowels)).upper()))

    if len(consonants) > 0:
        print('Guessed Consonants: {}'.format(' '.join(sorted(consonants)).upper()))


def is_word_complete(game_word, guessed_letters):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    is_complete = True
    for char in game_word:
        if char not in guessed_letters:
            is_complete = False
    return is_complete


def evil_word_selector(game_word, guessed_letters, evil_list):
    '''
    evil_list begins as a list of words that are of game_word length.
    1. A new random generator is needed for this version; choose word length only.
         - Need to look at distribution of words at different lengths to see
           what length should be the upper cutoff for game play
    2. Because we are going to return the pared down list, we need only assess
       the incoming letter.
    3. Look at the incoming list and make two lists for each empty position:
         a. one that has the guessed letter (yes_guessed_letter)
            - requires that each word be checked for duplicates that might
                  interfere with non-blanks.
            - any word that has duplicates must then be checked against the number
              of words left after the duplicated position has been filled
         b. one that does not have the guessed letter (no_guessed_letter)
    4. Assess which list is largest.
    5. If the larger of the lists includes the guessed letter, include it,
         otherwise, exclude it.
    '''
    word_template = display_word(game_word, guessed_letters[:-1])
    evil_options = []
    evil_options[0] = evil_list[:]

    # Make a list of lists, each containing narrower set of the last
    for i, char in enumerate(word_template):
        if char != '_':
            for word in evil_options[i]:
                if char == word[i]:
                    evil_options[i+1].extend(list(word))

    # Make a selection from the pared down list
    while True:
        evil_word = random_word(evil_options[-1])
        if evil_word = game_word

    return evil_word, evil_options[-1]


# def evil_list_reducer(word_template, prev_guessed_letters, evil_list):
#
#     return reduced_evil_list


def game_mode(word_list):
    '''Queries user for game mode and returns game_word'''
    game_word = ''
    while True:
        print("\nPlease select your level of difficulty (press Q to quit):")
        difficulty_level = input( "[E]asy, [M]edium, or [H]ard\n> ").lower()
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
    return game_word


def game_loop(game_word, width):
    guessed_letters = []    # holds letters guessed by the user
    allowed_guesses = 8     # number of guesses allotted to user per game (8)
    num_guesses = 0         # number of expended user guesses
    play_again = False      # records whether user wants to play again
    # MAIN GAME LOOP
    while len(game_word) != 0 and num_guesses < allowed_guesses:
        # Print current state of word with underscores for unguessed letters
        print('\n')
        print(display_word(game_word, guessed_letters).center(width))
        # print("Test: {}".format(game_word)) # TEST TO REMOVE
        print('\n\nYou have {} guesses remaining.'.format(allowed_guesses - num_guesses))

        # Get guess from user and add to guessed_letters list
        guessed_letters.append(user_guess(guessed_letters, width))

        # Add to guess tally if letter is not in game_word
        if guessed_letters[-1] not in game_word:
            num_guesses += 1

        # Show guessed letters
        show_guessed_letters(guessed_letters)

        if is_word_complete(game_word, guessed_letters):
            print(display_word(game_word, guessed_letters).center(width))
            win_msg = '    You win!    '.upper()
            win_fill = (width - len(win_msg)*3)//4
            extra_bit = width - len(win_msg)*3 - 4*win_fill
            print(('\n'*4+('='*win_fill+win_msg)*3+'='*(win_fill+extra_bit))+'\n\n')
        elif num_guesses >= allowed_guesses:
            print(display_word(game_word, guessed_letters).center(width))
            no_guesses_msg = 'You have run out of guesses'.upper()
            no_guesses_fill = (width - len(no_guesses_msg))//2
            print('\n'*4+'_'*no_guesses_fill+no_guesses_msg+'_'*no_guesses_fill)
            print('\nThe word you were trying to guess was: {}\n\n'.format(game_word.upper()))

        if is_word_complete(game_word, guessed_letters) or num_guesses >= allowed_guesses:
            play_again = user_continue(width)
            break
        # Not sure if I need to return both; is there a way to return just one?
    return play_again, False


def user_guess(guesses, width):
    user_guess = ''
    while True:
        user_guess = input("\n"+"-"*width+"\nPlease guess a letter.\n> ").lower()
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


def user_continue(width):
    user_continue = ''
    continue_bool = False
    while True:
        user_continue = input("Play again? [Y/n]: ").lower()
        if user_continue == '' or user_continue == 'y':
            continue_bool = True
            break
        elif user_continue == 'n':
            continue_bool = False
            goodbye_msg = "Goodbye".upper()
            goodbye_fill = (width - len(goodbye_msg))//2
            print('\n\n'+'_'*goodbye_fill+goodbye_msg+'_'*goodbye_fill+'\n\n')
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
    play_again = False      # records whether player wants to play again
    game_start = True       # records whether the game has been played yet
    width = 80              # default width
    height = 24             # default height
    terminal_info = {}      # dictionary to recieve terminal info from system

    terminal_info = get_terminal_size()
    if terminal_info[0] > 0:
        width = terminal_info[0]
    if terminal_info[1] > 0:
        height = terminal_info[1]

    while True:
        if game_start:
            # Read in entire dictionary
            with open('/usr/share/dict/words') as f:
                word_list = f.read().split()

            # Print welcome
            print('?'*width)
            welcome = 'Welcome to Mystery Word!'.upper()
            fill_half = (width - len(welcome) - 2)//2
            print(('?' + ' '*(width-2) + '?')*((height-7)//3))
            print( '?' + ' '*fill_half + welcome + ' '*fill_half+'?')
            print(('?' + ' '*(width-2) + '?\n')*((height-7)*2//3))

        # Get game word
        game_word = game_mode(word_list)

        # Run game loop
        play_again, game_start = game_loop(game_word, width)

        if play_again:
            continue
        else:
            break


if __name__ == '__main__':
    main()
