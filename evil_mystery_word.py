import random
from os import get_terminal_size


def easy_words():
    """
    Returns empty constraints 4-6 characters long.
    """
    length = random.randint(4,7)
    constraints = init_constraint(length)
    return ''.join(constraints)


def medium_words():
    """
    Returns empty constraints 6–8 characters long.
    """
    length = random.randint(6,9)
    constraints = init_constraint(length)
    return ''.join(constraints)


def hard_words(word_list):
    """
    Returns empty constraints between 8 and dict_max characters.
    """
    dict_max = 0
    for word in word_list:
        if len(word) > dict_max:
            dict_max = len(word)

    length = random.randint(8, dict_max)
    constraints = init_constraint(length)
    return ''.join(constraints)


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return word_list[random.randint(0,len(word_list)+1)].lower()


def init_constraint(length):
    constraints = []
    for n in range(length):
        constraints.append('_')
    return ''.join(constraints)


def display_word(constraints):
    display = []
    display = ' '.join(list(constraints)).upper()
    return display


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


def is_word_complete(constraints):
    """
    Returns True if the constraints have no blanks left.
    """
    is_complete = False
    if '_' not in constraints:
        is_complete = True
    return is_complete


def evil_word_selector(constraints, guessed_letters, evil_word_list):
    '''Because we aren't using a single word, our "word" is constraints'''
    # dict of lists; key represents # of viable letter occurrences
    repeats = {0: {'words': []}} # may need 'pattern'='__*_'
    # was {0: {'words': [], 'use': False}}
    letter_count = 0   # number of viable letter occurences
    most_words = 0     # placeholder dictionary to hold
    selected_dict = {} # holds largest dictionary
    new_constraints = ''

    for word in evil_word_list:
        letter_count = list(word.lower()).count(guessed_letters[-1])
        if letter_count > 0 and len(word) == len(constraints):
            if not repeats.get(letter_count, False):
                repeats[letter_count] = {}
            useable_word, new_constraints = assess_open_slots(
                              word.lower(), guessed_letters[-1], constraints)
            if useable_word:
            # Now, put into a list keyed with the new constraint
            #(e.g., if our letter is 'e', the key would be '_e__')
                if not repeats[letter_count].get(new_constraints, False):
                    repeats[letter_count][new_constraints] = []
                repeats[letter_count][new_constraints].append(word.lower())
        elif len(word) == len(constraints):
            repeats[0]['words'].append(word) # list of words without guessed letter

    # print(repeats)
    # Assess length of lists
    for num_repeats, num_repeats_dict in repeats.items():
        for constraints_pattern, words in num_repeats_dict.items():
            if len(words) > most_words:
                most_words = len(words)
                selected_dict = {'new_constraints': constraints_pattern,
                                 'words': words, 'length': len(words)}

    # # Make decision about how to proceed
    if selected_dict['length'] == len(repeats[0]['words']):
        evil_word_list = repeats[0]['words']
        new_constraints = constraints
    else:
        evil_word_list = selected_dict['words']
        new_constraints = selected_dict['new_constraints']

    # print("New constraints: {}\nGuessed letters: {}\nRemaining words: {}".format(
    #     new_constraints, guessed_letters, evil_word_list))
    return new_constraints, guessed_letters, evil_word_list


def assess_open_slots(word, letter, constraints):
    available_indices = []
    usable = True
    new_constraints = list(constraints)

    for constraint_index, constraint_char in enumerate(list(constraints)):
        if constraint_char == '_':
            available_indices.append(constraint_index)

    for index, char in enumerate(list(word.lower())):
        if letter == char:    # look for location of guess letter in word
            if index not in available_indices: # letter can only appear in '_' slots:
                new_constraints = list(constraints)
                return False, constraints
            else:
                new_constraints[index] = letter

    return usable, ''.join(new_constraints)


def game_mode(word_list):
    '''Queries user for game mode and returns constraints'''
    constraints = ''
    while True:
        print("\nPlease select your word length level of difficulty (press Q to quit):")
        difficulty_level = input( "[E]asy (4-6), [M]edium (6-8), or [H]ard (8+)\n> ").lower()
        if difficulty_level == 'e':
            constraints = easy_words()
            break
        elif difficulty_level == 'm':
            constraints = medium_words()
            break
        elif difficulty_level == 'h':
            constraints = random_word(hard_words(word_list))
            break
        elif difficulty_level == 'q':
            break
        else:
            print("\nInvalid selection.")
            continue
    return constraints


def game_loop(constraints, width, word_list):
    guessed_letters = []    # holds letters guessed by the user
    allowed_guesses = 8     # number of guesses allotted to user per game (8)
    num_guesses = 0         # number of expended user guesses
    play_again = False      # records whether user wants to play again
    # MAIN GAME LOOP
    while len(constraints) != 0 and num_guesses < allowed_guesses:
        # Print current state of word with underscores for unguessed letters
        print('\n')
        print(display_word(constraints).center(width))
        print('\n\nYou have {} guesses remaining.'.format(allowed_guesses - num_guesses))

        # Get guess from user and add to guessed_letters list
        guessed_letters.append(user_guess(guessed_letters, width))

        # Run the evil_word_selector
        constraints, guessed_letters, word_list = evil_word_selector(
            constraints, guessed_letters, word_list)
        if guessed_letters[-1] not in constraints:
            num_guesses += 1

        # Show guessed letters
        show_guessed_letters(guessed_letters)

        if is_word_complete(constraints):
            print(display_word(constraints).center(width))
            win_msg = '    You win!    '.upper()
            win_fill = (width - len(win_msg)*3)//4
            extra_bit = width - len(win_msg)*3 - 4*win_fill
            print(('\n'*4+('='*win_fill+win_msg)*3+'='*(win_fill+extra_bit))+'\n\n')
        elif num_guesses >= allowed_guesses:
            print(display_word(constraints).center(width))
            no_guesses_msg = 'You have run out of guesses'.upper()
            no_guesses_fill = (width - len(no_guesses_msg))//2
            print('\n'*4+'_'*no_guesses_fill+no_guesses_msg+'_'*no_guesses_fill)
            print('\nThe word you were trying to guess was: {}\n\n'.format(
                   random_word(word_list).upper()))

        if is_word_complete(constraints) or num_guesses >= allowed_guesses:
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
    constraints = ''          # holds random word from specified game mode
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
        constraints = game_mode(word_list)

        # Run game loop
        play_again, game_start = game_loop(constraints, width, word_list)

        if play_again:
            continue
        else:
            break


if __name__ == '__main__':
    main()
