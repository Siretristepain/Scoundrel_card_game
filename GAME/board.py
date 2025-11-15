# ========================
# Implement the game board
# ========================

from cards import Card
from deck import Deck, get_standard_deck

class Board():

    def __init__(self, deck: Deck=None, discard: Deck=None, slot_1: Card=None, slot_2: Card=None, slot_3: Card=None, slot_4: Card=None, weapon: Card=None):

        # We link the Deck/Discard to the board
        self.deck = deck
        self.discard = discard

        # The 4 slots Cards for the room
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        self.slot_3 = slot_3
        self.slot_4 = slot_4

        # The equiped weapon
        self.weapon = weapon

    def __repr__(self):
        """
        Get a simple stdout of the Board. Could be improve next.

        TODO : Add the player's life (only once I've create the Player class).
        """
        return f"\n| {self.slot_1} | {self.slot_2} | {self.slot_3} | {self.slot_4} | \n \n\
        | {self.weapon} |\n"

    def get_room(self):
        """
        Method which fill the 4 slots Cards of the Board by draw 4 times in a row.

        TODO : At the point, no verificatin is done about the posibility to draw (imagine if it's remains only 1 Card in the Deck?).
               + This version is good for the first room and the rooms after passing one, but in "normal" case, we have to draw only 3 times.

        Returns:
            - (bool) : True.
        """
        self.slot_1 = self.deck.draw()
        self.slot_2 = self.deck.draw()
        self.slot_3 = self.deck.draw()
        self.slot_4 = self.deck.draw()
        return True

    def clear_slots(self):
        """
        Method used to "clear" the 4 slots of Cards of the Board.
        It put each slot to None.

        Returns:
            - (bool) : True.
        """
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None
        self.slot_4 = None
        return True

    def pass_room(self):
        """
        Method used to implement the "pass room" logic.
        First it put the Cards of the room at the bottom of the Deck and then clear the slots.

        Be careful, this method does not get the new room!
        """
        # First, put the Card of the Board at T time at the bottom of the Deck
        for card in [self.slot_1, self.slot_2, self.slot_3, self.slot_4]:
            bottom_card = self.deck.get_last_card()
            bottom_card.next = card
        self.clear_slots()

        return True

    def black_card_on_board(self):
        """
        Method used to check if there is at least one black Card on Board.

        Returns:
            - (list) : True if at least one black Card on Board, False otherwise.
        """
        return self.slot_1.is_black() or self.slot_2.is_black() or self.slot_3.is_black() or self.slot_4.is_black()

if __name__ == "__main__":

    deck = get_standard_deck()
    board = Board()
    board.deck = deck
    # print(board)

    # Get a first room and print it
    board.get_room()
    print(board)

    # Pass the room and print the empty room
    board.pass_room()
    print(board)

    # Get a new room and print it
    board.get_room()
    print(board)

    print(board.deck)
    board.slot_1 = Card('2', 'Spades')
    print(board)
    print(board.black_card_on_board())
