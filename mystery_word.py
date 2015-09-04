import random


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
    return word_list[random.randint(0,len(word_list))]


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
    # TODO
    pass


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
    guessed_letters = ''    # holds letters guessed by the user
    temp_guess = ''         # temp variable to hold user input in MAIN GAME LOOP
    num_guesses = 8         # number of guesses allotted to user per game

    # Read in entire dictionary
    with open('/usr/share/dict/words') as f:
        word_list = f.read().split()

    print("\n"+('#'*10+"    Welcome to Mystery Word!    "+'#'*10).upper().center(55)+"\n")

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
    while len(game_word) != 0 and num_guesses > 0:
        #TODO
        guessed_letters.append(user_guess())


    print(display_word(game_word, 'abcdefg').center(55))


if __name__ == '__main__':
    main()
