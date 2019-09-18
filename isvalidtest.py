import unittest
from spaceman import valid_input


class test_valid(unittest.TestCase):
    """Unit Test for function: valid_input()

    @Attributes:
        funciton test_singe_char(): Tests function: valid_input() by passing a single character and checking the returned boolean value
        function test_non_string(): Tests function: valid_input() by passing an integer and checking the returned boolean value
        function test_multiple_char(): Tests function: valid_input() by passing a string of characters and checking the returned boolean value
        function test_empty(): Tests function: valid_input() by passing an empty string and checking the returned boolean value
    """

    def test_single_char(self):
        """ >>> valid_input('b')
            >>> True 
        """
        self.assertTrue(valid_input('b'), True)  # single character b

    def test_non_string(self):
        """ >>> valid_input(90)
            >>> False 
        """
        self.assertFalse(valid_input(90), False)  # pass integer argument

    def test_multiple_char(self):
        """ >>> valid_input('fiuewy')
            >>> False 
        """
        self.assertFalse(valid_input('fghsja'),
                         False)  # pass more than one letter

    def test_empty(self):
        """ >>> valid_input('')
            >>> False
        """
        self.assertFalse(valid_input(""), False)  # pass empty string


if __name__ == "__main__":
    unittest.main()
