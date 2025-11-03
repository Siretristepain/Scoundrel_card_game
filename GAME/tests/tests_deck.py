import unittest

# We add the 'GAME' folder to Python Path (-> location where Python search for modules)
import sys
sys.path.append('GAME')

from cards import Card
from deck import Deck

class TestCardMethods(unittest.TestCase):

    def setUp(self):
        
        # Empty Deck
        self.D0 = Deck()

        # Collection of Cards
        self.C1 = Card('2', 'Diamonds')
        self.C2 = Card('5', 'Spades')
        self.C3 = Card('Q', 'Hearts')

        self.C4 = Card('K', 'Clubs')

        self.C1.next = self.C2
        self.C2.next = self.C3

        # Deck with 3 Cards
        self.D1 = Deck(head=self.C1)

        return super().setUp()
    
    def test_is_empty(self):
        """
        Test Deck.is_empty() method.
        """
        self.assertTrue(self.D0.is_empty())
        self.assertFalse(self.D1.is_empty())

    def test_get_size(self):
        """
        Test Deck.get_size() method.
        """
        self.assertEqual(self.D0.get_size(), 0)
        self.assertEqual(self.D1.get_size(), 3)

        # Check size of the Deck after adding a Card
        self.D1.add_card(self.C4)
        self.assertEqual(self.D1.get_size(), 4)

        # Check size of the Deck after remove a Card
        self.D1.remove_card(self.C4)
        self.D1.remove_card(self.C3)
        self.assertEqual(self.D1.get_size(), 2)


if __name__ == '__main__':
    unittest.main()
