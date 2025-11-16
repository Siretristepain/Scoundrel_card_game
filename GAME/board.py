# ========================
# Implement the game board
# ========================

from cards import Card
from deck import Deck, get_standard_deck
from player import Player

class Board():

    def __init__(self, player: Player=None, deck: Deck=None, discard: Deck=None, slot_1: Card=None, slot_2: Card=None, slot_3: Card=None, slot_4: Card=None, weapon: Card=None):

        # We link a Player to the Board
        self.player = player

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

        Returns:
            - (str) : the Board (each slots, weapon and Player's life).
        """

        return f"\n| {self.slot_1} | {self.slot_2} | {self.slot_3} | {self.slot_4} | \n \n\
        | {self.weapon} |    life : {self.player.life}/{self.player.max_life}\n"

    def get_room(self):
        """
        Method which fill the 4 slots Cards of the Board by draw 4 times in a row.
        This method only fill empty slot, so if a slot is already fill before call the method, the Card inside is not replace.

        Returns:
            - (bool) : True.
        """

        # Before draw, we check each slot if it's empty.
        if not self.slot_1:
            self.slot_1 = self.deck.draw()

        if not self.slot_2:
            self.slot_2 = self.deck.draw()

        if not self.slot_3:
            self.slot_3 = self.deck.draw()

        if not self.slot_4:
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

    def get_cards_on_board(self):
        """
        Method used to get a list of all the Card instance on the room (~Board).
        The main goal of this method is to don't have issue when a slot is empty (NoneType).

        Returns:
            - cards (list[Card]) : list of Card that compose the current room (with no NoneType).
        """
        cards = [card for card in [self.slot_1, self.slot_2, self.slot_3, self.slot_4] if card != None]
        return cards

    def black_card_on_board(self):
        """
        Method used to check if there is at least one black Card on Board.

        Returns:
            - (bool) : True if at least one black Card on Board, False otherwise.
        """
        # We get a list of all the Cards in the room (without taking empty slots).
        cards = self.get_cards_on_board()

        # For all these Cards, we check if there's at least one black Card.
        for card in cards:
            if card.is_black():
                return True
        return False

    def check_victory(self):
        """
        Method used to check if the Player wins.
        Wins means : no black Card on Deck AND no black Card on Board.

        Returns:
            - (bool) : True if no black Cards left (both Deck and Board), False otherwise.
        """
        if not self.black_card_on_board() and not self.deck.has_black_card():
            return True
        return False

    def check_defeat(self):
        """
        Method used to check if the Player lose.
        Lose means : Player's life reach 0.

        player.is_alive = True so return False
        player.is_alive = False so return True

        Returns:
            - (bool) : True is the Player lose, False otherwise.
        """
        return not self.player.is_alive()

if __name__ == "__main__":

    # deck = get_standard_deck()

    # PLAYER
    player = Player('John', life=0)

    # CARDS (and relations)
    C1 = Card('2', 'Diamonds')
    C2 = Card('Q', 'Hearts')
    C3 = Card('K', 'Diamonds')
    C4 = Card('6', 'Hearts')

    C1.next = C2

    # DECK
    deck = Deck()
    deck.head = C1

    # BOARD
    board = Board()
    board.deck = deck
    board.player = player

    board.slot_4 = C3
    print(board)

    # ACTIONS
    board.get_room()
    print(board)
