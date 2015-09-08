import unittest
from evil_mystery_word import *

word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain",
             'goat', 'moat', 'boat', 'goal', 'mode', 'boar', 'goad',
             'goag', 'goaf', 'goam']
constraints = '__a_'
guessed_letters = []
guessed_letters.append('g')
new_constraints = ''
evil_word_list = word_list[:]

class TestEvilMysteryWord(unittest.TestCase):

    def evil_word_selector(self):
        # new_constraints, evil_word_list = evil_word_selector(constraints, guessed_letters, word_list)
        self.assertEqual(evil_word_selector(constraints, guessed_letters, word_list), ('g_a_', ["goat", "goal", "goad", "goag", "goaf", "goam"]))


    # def test_random_word(self):
    #     """This test is not very good. Testing things that are random is hard,
    #     in that there's not a predictable choice. The best we can do is make
    #     sure we have valid output."""
    #     word = random_word(word_list)
    #     self.assertTrue(word in word_list)


    # def test_display_word(self):
    #     word = "integration"
    #     self.assertEqual(display_word(word, []), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["z"]), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["g"]), "_ _ _ _ G _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["i"]), "I _ _ _ _ _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "g"]), "I _ _ _ G _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "n", "z"]), "I N _ _ _ _ _ _ I _ N")
    #
    #
    # def test_is_word_complete(self):
    #     word = "river"
    #     self.assertFalse(is_word_complete(word, []))
    #     self.assertFalse(is_word_complete(word, ["r"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e", "z"]))
    #     self.assertTrue(is_word_complete(word, ["r", "e", "v", "i"]))

if __name__ == '__main__':
    unittest.main()
