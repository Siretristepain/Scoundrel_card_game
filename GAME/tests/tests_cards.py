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
        self.C7 = Card('Q', 'Clubs')
        self.C8 = Card('Joker')
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

    def test_is_eaven(self):
        """
        Test the Card.is_eaven() method.
        """
        self.assertFalse(self.C3.is_eaven())
        self.assertFalse(self.C6.is_eaven())
        self.assertTrue(self.C4.is_eaven())

    def test_is_odd(self):
        """
        Test the Card.is_odd() method.
        """
        self.assertFalse(self.C6.is_eaven())
        self.assertFalse(self.C2.is_odd())
        self.assertTrue(self.C5.is_odd())

    def test_is_red(self):
        """
        Test the Card.is_red() method.
        """
        self.assertTrue(self.C2.is_red())
        self.assertTrue(self.C6.is_red())
        self.assertFalse(self.C3.is_red())
        self.assertFalse(self.C4.is_red())

    def test_is_black(self):
        """
        Test the Card.is_black() method.
        """
        self.assertTrue(self.C3.is_black())
        self.assertTrue(self.C4.is_black())
        self.assertFalse(self.C2.is_black())
        self.assertFalse(self.C2.is_black())

    def test_is_joker(self):
        """
        Test Card.is_joker() method.
        """
        self.assertFalse(self.C6.is_joker())
        self.assertTrue(self.C8.is_joker())

    def test_is_greater(self):
        """
        Test Card.is_greater() method.
        """
        # Test Q > 2
        self.assertTrue(self.C6.is_greater(self.C2))

        # Test 5 > 3
        self.assertTrue(self.C5.is_greater(self.C3))

        # Test 2 > 4
        self.assertFalse(self.C2.is_greater(self.C4))

    def test_is_lower(self):
        """
        Test Card.is_lower() method.
        """
        # Test 2 < 5
        self.assertTrue(self.C2.is_lower(self.C5))

        # Test 5 < Q
        self.assertTrue(self.C5.is_lower(self.C6))

        # Test Q < 4
        self.assertFalse(self.C6.is_lower(self.C4))

    def test_is_equal(self):
        """
        Test Card.is_equal() method.
        """
        self.assertTrue(self.C6.is_equal(self.C7))
        self.assertFalse(self.C2.is_equal(self.C5))

if __name__ == '__main__':
    unittest.main(verbosity=2)
