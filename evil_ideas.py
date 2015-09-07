def evil_word_selector(constraints, guessed_letters, evil_word_list):
    '''Because we aren't using a single word, our "word" is constraints'''
    repeats = {}      # dict of lists; key represents # of viable letter occurrences
    letter_count = 0  # number of viable letter occurences
    list_counter = {}

    for word in evil_word_list:
        letter_count = list(word).count(guessed_letters[0][-1])
        if letter_count > 0:
            if assess_open_spots(word, constraints, guessed_letters):
                repeats[letter_count]['words'].extend([word])
        else:
            repeats[0]['words'].extend([word]) # represents list of words without guessed letter

        # Assess relative lengths of initial pass
        for num_repeats, word_list in repeats.items():
             list_counter[num_repeats] = len(repeats[num_repeats])

            len(repeats[0]) >= len(repeats[1]):
                evil_word_list = repeats[0][:]
        else:
            # Start assessment of duplicates
            while True:


    return evil_word_list, guessed_letters, constraints

def assess_open_slots(word, letter, constraints, repeats):
    if # letter only appears in '_' slots:
        return True, repeats
    else:
        return False, repeats


constraints = display_word(guessed_letters[1])

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
