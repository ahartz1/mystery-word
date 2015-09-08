# Mystery Word

### Do you love 'hangman' word games?

#### System Requirements

* Must have dictionary at **/usr/share/dict/words** on your system. Mac&nbsp;OS&nbsp;X users should have this on their system by default.

* You will need to have **python&nbsp;3** installed on your machine or have access to a python&nbsp;3 interpreter. See [python's site](https://www.python.org/) for details.

* To run this program, save `mystery_word.py` to your computer. Using a command-line program (such as Terminal on Mac&nbsp;OS&nbsp;X), navigate to the folder containing the downloaded file and run the following line to play: `python3 mystery_word.py`

* This program uses the os.terminal_info function to retrieve the size of your terminal window to appropriately scale the output. If this environment variable is not accessible on your system, the output size defaults to 80 columns x 24 rows.

#### Game Description
Much like hangman, you guess letters in an effort to uncover a word randomly selected from the dictionary. Once you select your difficulty level, each letter in the word is represented by an underscore. As you guess letters correctly, they replace the underscores (e.g., `_ _ A _ _`). You have only **8 guesses**, but if you select a letter that is in the word, **you do not lose a guess**. (Also, you don't lose a guess if you accidentally guess a letter you've already guessed.) Your number of remaining guesses is displayed each round, along with the vowels and consonants that you have already guessed.

##### Choose your word length difficulty
Easy | Medium | Hard
|:---:|:---:|:---:|
4–6 | 6–8 | 8+

##### A word about the dictionary
The words used in this game are from web2 (Webster's Second International) dictionary, copyright 1934. The copyright has lapsed, and thus is in the public domain. Keep an open mind and get ready to learn some new words as you play!

# Evil Mystery Word

#### System Requirements
Same as for Mystery Word, except the filename is `evil_mystery_word.py`.

#### Game Description
Gameplay is the same as for Mystery Word, but the inner workings have changed to make the game more challenging (OK, nearly impossible). The computer actively works against the player by finding words fitting the display pattern (e.g., `_ _ Y _ _ _ _` ), to avoid having the guessed letters appear in the word.
