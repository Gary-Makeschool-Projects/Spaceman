import unittest
from spaceman import is_guess_in_word


class test_word_guessed(unittest.TestCase):
    """Unit Test for function: is_guess_in_word()

    @Attributes:
        funciton test_correct: Tests function: is_guess_in_word() by comparing a random word to a single character that is inside 'word'
        function test_incorrect(): Tests function: is_guess_in_word() by comparing a random word to a single character that is not inside 'word'
        function test_empty(): Tests function: is_guess_in_word() by comparing a random word to an empty string
        function test_integer(): Tests function: is_guess_in_word() by comparing a random word an integer
    """

    def test_correct(self):
        """ >>> is_guess_in_word('a' 'waffles')
            >>> True
        """
        word = 'waffles'
        guess = 'a'
        self.assertTrue(is_guess_in_word(guess, word), True)

    def test_incorrect(self):
        """ >>> is_guess_in_word('y', 'Alan')
            >>> False
        """
        word = 'Alan'
        guess = 'y'
        self.assertFalse(is_guess_in_word(guess, word), False)

    def test_empty(self):
        """ >>> is_guess_in_word('break', '')
            >>> False
        """
        word = 'break'
        guess = ''
        self.assertFalse(is_guess_in_word(guess, word), False)

    def test_integer(self):
        """ >>> is_guess_in_word(90, 'cat')
            >>> False
        """
        word = 'cat'
        guess = 90
        self.assertFalse(is_guess_in_word(guess, word), False)


if __name__ == "__main__":
    unittest.main()
