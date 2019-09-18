import unittest
from spaceman import is_word_guessed


class test_word_guessed(unittest.TestCase):
    """Unit Test for function: is_word_guessed()

    @Attributes:
        funciton test_all_words: Tests function: is_word_guessed() by comparing a random word to an array complete with all letters that creates 'word' 
        function test_partial(): Tests function: is_word_guessed() by comparing a random word to an array containg a partial amount of letters that creat 'word'
        function test_empty(): Tests function: is_word_guessed() by comparing a random word to an empty array
        function test_arr_of_integers(): Tests function: is_word_guessed() by comparing a random word to an array of integers
    """

    def test_all_words(self):
        """ >>> is_word_guessed("happy", ['h','p','p','a','y'])
            >>> True 
        """
        word = 'happy'
        arr = ['h', 'p', 'p', 'a', 'y']
        self.assertTrue(is_word_guessed(word, arr),
                        True)  # try all letters of and array containing all letters of the word

    def test_partial(self):
        """ >>> is_word_guessed('cat, ['a','t'])
            >>> False 
        """
        word = 'cat'
        arr = ['a', 't']
        self.assertFalse(is_word_guessed(word, arr), False)

    def test_empty(self):
        """ >>> is_word_guessed('bacon', [])
            >>> False 
        """
        word = 'bacon'
        arr = []
        self.assertFalse(is_word_guessed(word, arr), False)

    def test_arr_of_integers(self):
        """ >>> is_word_guessed('cat, ['1','79'])
            >>> False 
        """
        word = 'gary'
        arr = [1, 79]
        self.assertFalse(is_word_guessed(word, arr), False)


if __name__ == "__main__":
    unittest.main()
