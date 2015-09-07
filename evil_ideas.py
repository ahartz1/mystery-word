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
        letter_count = list(word.lower()).count(guessed_letters[0][-1])
        if letter_count > 0:
            useable_word, new_constraints = assess_open_slots(word.lower(), guessed_letters[0][-1], constraints)
            if useable_word:
            # Now, put into a list keyed with the new constraint
            #(e.g., if our letter is 'e', the key would be '_e__')
                if not repeats[letter_count].get(new_constraints, False):
                    repeats[letter_count] = {new_constraints: []} #TODO
                repeats[letter_count][new_constraints].append(word.lower())
        else:
            repeats[0]['words'].append(word) # list of words without guessed letter

    print(repeats)
    # Assess relative lengths of initial pass
    # for num_repeats, num_repeats_dict in repeats.items():
    #     num_repeats_dict['length'] = len(num_repeats_dict['words'])
    #     if num_repeats_dict['length'] > most_words:
    #         most_words = num_repeats_dict['length']
    #         selected_dict = num_repeats_dict
    #
    # # Make decision about how to proceed
    # if selected_dict['length'] == repeats[0]['length']:
    #     evil_word_list = repeats[0]['words']
    # else:
    #     # Start assessment of duplicates
    #     # while True:
    #     print("I made it here!")

    # print(repeats)
    # print("Letter: {}\nTotal words: {}".format(guessed_letters[0][-1], len(evil_word_list)))
    # print(evil_word_list)
    # TODO Make sure you have updated constraints to new_constraints if necessary
    return constraints, guessed_letters, evil_word_list

def assess_open_slots(word, letter, constraints):
    available_indices = []
    usable = True
    new_constraints = list(constraints)

    for constraint_index, constraint_char in enumerate(list(constraints)):
        if constraint_char == '_':
            available_indices.append(constraint_index)

    for index, char in enumerate(list(word)):
        if letter == char:    # look for location of guess letter in word
            if index not in available_indices: # letter can only appear in '_' slots:
                new_constraints = list(constraints)
                return False, constraints
            else:
                new_constraints[index] = letter

    return usable, ''.join(new_constraints)

evil_word_list = ['goat', 'moat', 'boat',
                  'goal', 'mode', 'boar',
                  'goad', 'goag', 'goaf']
constraints = '__a_'
guessed_letters = [[],[]]
guessed_letters[0].append('g')

evil_word_selector(constraints, guessed_letters, evil_word_list)

'''
Gameplay Ideas:
It might be nice to output how many words were eliminated from the total for each
guess. Also, show the remaining words over the total number of words in the
dictionary; display the percentage of words remaining and percentage eliminated
by previous letter guessed.
'''

'''
evil_word_selector optimization ideas:
If any list of duplicates is longer than both the non-letter-containing list and
the single-letter-containing list:
  - Instead of looking at all permutations, use an empirical approach: take the
    first word and look for the number of other words in the list with that
    configuration of duplicates. Then, assess the length of that list against the
    next longest list (first time around, this would be the single-letter-containing
    list because the non-letter-containing list has to be shorter to start the
    evaluation process to begin with.
      - If the empirical list is longer than both, check to see if the length
        of empirical list is longer than the remaining list. If so, empirically
        assess the next word in the list. When the remaining list is shorter than
        the longest currently known list, stop processing.
  - During the evaluation process, remove each empirically assessed word from the
    list; this will reduce complexity and reduce processing time.
'''

'''
guessed_letters may now need to be a list containing two lists: the current guessed
letter and the letters used; guessed_letters[0] and guessed_letters[1], respectively.
  - Is this necessary? We will already be returning a list that eliminates the
    previously guessed letters, so no need to keep track of them.
    - Yes, we will need a place to store the current guess and all guessed letters.
'''

'''
list_lengths will be a dictionary.
  - key=0 will be for length of list without letter
  - key=1 will be for length of list with letter (regardless of how many duplicates)
      - used for first round assessment
  - key='empirical display' (e.g., "_ _ E _")
      - each of these are created only when length of other lists are considered
'''

'''
constraints will be defined as a list with index corresponding to position in
word of game_word length. Unfilled slots have a value of '_', filled slots have
the value of the letter present.
'''
