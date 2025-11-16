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

        # Check size of empty Deck
        self.assertEqual(self.D0.get_size(), 0)

    def test_get_first_card(self):
        """
        Test Deck.get_first_card() method.
        """
        # Empty Deck case
        self.assertEqual(self.D0.get_first_card(), None)

        # Standard case
        self.assertEqual(self.D1.get_first_card(), self.C1)

        # Get the first Card after add a new top Card
        self.D1.add_top_card(self.C4)
        self.assertEqual(self.D1.get_first_card(), self.C4)

    def test_get_last_card(self):
        """
        Test Deck.get_last_card() method.
        """
        # Empty Deck case
        self.assertEqual(self.D0.get_last_card(), None)

        # Standard case
        self.assertEqual(self.D1.get_last_card(), self.C3)

        # Get the last Card after add a new bottom Card
        self.D1.add_bottom_card(self.C4)
        self.assertEqual(self.D1.get_last_card(), self.C4)

    def test_get_card(self):
        """
        Test Deck.get_card() method.
        """
        # Empty Deck case
        self.assertEqual(self.D0.get_card(index=2), None)

        # Out of range case
        self.assertEqual(self.D1.get_card(index=6), None)

        # Standard case
        # index :  0   1   2
        # D1    : C1  C2  C3
        self.assertEqual(self.D1.get_card(index=2), self.C3)

    def test_have_in(self):
        """
        Test Deck.have_in() method.
        """
        # Test empty Deck case
        self.assertEqual(self.D0.have_in(target_card=self.C4), False)

        # Standard case
        self.assertEqual(self.D1.have_in(target_card=self.C1), True)

        # Check after remove the target Card
        self.D1.remove_card(card_to_remove=self.C1)
        self.assertEqual(self.D1.have_in(target_card=self.C1), False)

    def test_add_top_card(self):
        """
        Test Deck.add_top_card() method.
        """
        # Test adding a NoneType at top of an empty Deck
        self.assertEqual(self.D0.add_top_card(card_to_add=None), False)
        self.assertEqual(self.D0.get_first_card(), None)

        # Standard case
        self.assertEqual(self.D0.add_top_card(card_to_add=self.C4), True)
        self.assertEqual(self.D0.get_first_card(), self.C4)

        # Test adding a NoneType at top of a filled Deck
        self.assertEqual(self.D1.add_top_card(card_to_add=None), False)
        self.assertEqual(self.D1.get_first_card(), self.C1)

    def test_add_bottom_card(self):
        """
        Test Deck.add_bottom_card() method.
        """
        # Test adding a NoneType at the bottom of an empty Deck
        self.assertEqual(self.D0.add_bottom_card(card_to_add=None), False)
        self.assertEqual(self.D0.get_last_card(), None)

        # Standard case
        self.assertEqual(self.D0.add_bottom_card(card_to_add=self.C4), True)
        self.assertEqual(self.D0.get_last_card(), self.C4)

        # Test adding a NoneType at the bottom of a filled Deck
        self.assertEqual(self.D1.add_bottom_card(card_to_add=None), False)
        self.assertEqual(self.D1.get_last_card(), self.C3)

    def test_add_card(self):
        """
        Test Deck.add_card() method.
        """
        # Standard case (try add a new Card at the second position in a Deck composed of 3 Cards)
        self.assertEqual(self.D1.add_card(card_to_add=self.C4, index=1), True)
        self.assertEqual(self.D1.get_card(index=1), self.C4)

        # Try to add a NoneType at the second position of a Deck composed of 4 Cards
        self.assertEqual(self.D1.add_card(card_to_add=None, index=1), False)
        self.assertEqual(self.D1.get_card(index=1), self.C4)

        # Try to add a Card at the first position in an empty Deck
        self.assertEqual(self.D0.add_card(card_to_add=self.C4, index=0), True)
        self.assertEqual(self.D0.get_first_card(), self.C4)

        # Try to add a Card out of range of the Deck
        self.assertEqual(self.D0.add_card(card_to_add=self.C3, index=12), False)

        # Try to add a Card at the last position in a Deck
        size_of_deck = self.D0.get_size()
        self.assertEqual(self.D0.add_card(card_to_add=self.C3, index=size_of_deck), True)
        self.assertEqual(self.D0.get_last_card(), self.C3)

if __name__ == '__main__':
    unittest.main()
