def evil_word_selection(constraints, guessed_letters, evil_word_list):
    '''|_ Because we aren't using a single word, constraints is our "word" _|'''
    repeats = []
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
