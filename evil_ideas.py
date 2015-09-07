def evil_word_selector(constraints, guessed_letters, evil_word_list):
    '''Because we aren't using a single word, our "word" is constraints'''
    repeats = []  # list of lists; index represents the # of times letter appears
    for word in evil_word_list:
      letter_count = list(word).count(guessed_letters[0][-1])
      if letter_count > 0:
        assess_open_spots(word, guessed_letters[1][:])
      else:
        repeats[0].extend(list(guessed_letters[0][-1]))
      repeats[len(letter_count)].extend([word])

      return evil_word_list, guessed_letters, constraints

def assess_open_slots(word, constraints, guessed_letters, evil_word_list):
  pass


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
