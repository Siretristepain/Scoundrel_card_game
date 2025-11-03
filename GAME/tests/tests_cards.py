import unittest

# We add the 'GAME' folder to Python Path (-> location where Python search for modules)
import sys
sys.path.append('GAME')

from cards import Card

class TestCardMethods(unittest.TestCase):

    def setUp(self):
        """
        The setUp() method is trigger before each test.
        The objective here is to create a set of Cards usable in each tests bellow.
        (--> maybe search for a method that execute only one before all tests ?)
        """
        self.C1 = Card()
        self.C2 = Card('2', 'Diamonds')
        self.C3 = Card('3', 'Spades')
        self.C4 = Card('4', 'Clubs')
        self.C5 = Card('5', 'Hearts')
        self.C6 = Card('Q', 'Hearts')
        return super().setUp()

    def test_is_null(self):
        """
        Test the Card.is_null() method.
        """

        self.assertTrue(self.C1.is_null())
        self.assertFalse(self.C2.is_null())

    def test_is_face_card(self):
        """
        Test the Card.is_face_card() method.
        """
        self.assertFalse(self.C4.is_face_card())
        self.assertTrue(self.C6.is_face_card())

if __name__ == '__main__':
    unittest.main(verbosity=2)
