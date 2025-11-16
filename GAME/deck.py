# ======================
# Implement Deck() class
# ======================

import random
from cards import Card

class Deck():

    def __init__(self, head: Card = None):
        self.head = head

    def __repr__(self):
        return f"Deck composed of {self.get_size()} Cards : {self.get_list()}."

    def is_empty(self):
        """
        Method used to check if the Deck is empty.

        Returns:
            - (bool) : True if empty deck, False otherwise.
        """
        return self.head == None
    
    def get_size(self):
        """
        Method used to get the size of the Deck, it means the number of Cards in the Deck.

        Returns:
            - (int) : the size of the deck (the number of Cards in the deck).
        """

        # We initalize a counter 'size' to 0 and we increment +1 for each card in the Deck
        size = 0

        if self.is_empty():
            return size
        
        card = self.head
        size += 1

        while card.next:
            size += 1
            card = card.next

        return size
    
    def get_first_card(self):
        """
        Method used to get the first Card of the Deck (the top Card).

        Returns:
            - (Card) : the top Card object.
        """
        return self.head
    
    def get_last_card(self):
        """
        Method used to get the last Card of the Deck (the bottom Card).

        Returns:
            - card (Card) : the bottom Card object.
        """

        # If the Deck is empty, return None
        if self.is_empty():
            return None
        
        # Otherwise, go through all Cards until the last one (which have no next)
        card = self.head
            
        while card.next:
            card = card.next

        return card
    
    def get_card(self, index: int):
        """
        Method used to get the Card at the 'index' position in the Deck.

        Args:
            - index (int) : the position of the Card in the Deck we want to get.

        Returns:
            - card (Card()) : the Card at the 'index' position in the Deck. Could be None (ex: if we're out of range).
        """

        if self.is_empty():
            return None

        if index >= self.get_size():
            return None

        card = self.head

        for i in range(index):
            card = card.next

        return card

    def have_in(self, target_card: Card=None):
        """
        Method used to check if the 'target_card' is in the Deck.

        Args:
            - target_card (Card()) : the Card object that we want to check the presence in Deck.

        Returns:
            - (bool) : True if 'target_card' in Deck, False otherwise.
        """

        # We take the top Card of the Deck.
        card = self.head

        # We check if that first Card is the target one.
        if card == target_card:
            return True

        # We go through all the Card in the Deck and we always check if it's the target one.
        for i in range(self.get_size()):
            card = card.next

            if card == target_card:
                return True

        return False

    def add_top_card(self, card_to_add: Card=None):
        """
        Method used to add a Card at the top of the Deck.

        Args:
            - card_to_add (Card()) : the Card object to add to the top of the Deck.

        Returns:
            - (bool) : True if success, False if the Card to add is None or have no value.
        """

        # We don't add the Card if it's None or have a null value.
        if card_to_add == None or card_to_add.is_null():
            return False

        # We take the actual top Card (before adding) in order to make the 'card_to_add' pointer go to this one.
        actual_top_card = self.head

        # We put the new top Card
        self.head = card_to_add

        # We make the new top Card pointer to the older one.
        card_to_add.next = actual_top_card

        return True

    def add_bottom_card(self, card_to_add: Card=None):
        """
        Method used to add a Card at the bottom of the Deck.

        Args:
            - card_to_add (Card()) : the Card to add at the bottom.

        Return:
            - (bool) : True if success, False if the Card to add is None or have no value.
        """

        # We don't add the Card if it's None or have a null value.
        if card_to_add == None or card_to_add.is_null():
            return False

        # We get the last Card and make it's pointer go through 'card_to_add'.
        last_card = self.get_last_card()
        last_card.next = card_to_add

        return True

    def add_card(self, card_to_add: Card=None, index: int=0):
        """
        Method used to add a Card at the 'index' position in the Deck.
        Be careful, we start to count Card by index 0 (like Python standard list), so, for example, if you add a Card with index=5, it means that you're Card is
        the sixth Card of the Deck.

        Args:
            - card_to_add (Card) : the Card to add in the Deck.
            - index (int) : the position to add the Card in the Deck.

        Returns:
            - (bool) :
        """

        # TODO: prevent case if index = 0 (because then we call get_card(index-1) so it will be get_card(-1) --> Error.

        # We have to get the Card juste before the index that we want to add our Card (to change it's pointer and save it's older next).
        card_before = self.get_card(index-1)
        index_card_before_change = card_before.next

        # We put our new Card in the pointer of the previous Card and we make the pointer of our new Card to the older 'index' positionned Card.
        card_before.next = card_to_add
        card_to_add.next = index_card_before_change

        return True

    def get_index(self, card_to_find: Card=None):
        """
        Method used to get the index of the 'card_to_find' in the Deck.

        Args:
            - card_to_find (Card()) : the Card that we want to get the index.

        Returns:
            - i (int) : the index of the Card in the Deck, False if the Card is not found.
        """
        size = self.get_size()
        card = self.head

        for i in range(size):
            if card == card_to_find:
                return i
            card = card.next
            
        return None

    def remove_card(self, card_to_remove: Card=None):
        """
        Method used to remevo a 'card_to_remove' (Card) from the Deck.

        Args:
            - card_to_remove (Card()) : the Card that we want to remove.

        Returns:
            - (bool) : True if success, False otherwise (the Card is already not in the Deck).
            (maybe we want to return True even if the Card is not in the Deck?)
        """

        # TODO : prevent case if the Card that we want to delete is the first one because it will generate : get_card(-1)
        card_to_remove_index = self.get_index(card_to_find=card_to_remove)
        card_before = self.get_card(card_to_remove_index-1)
        card_before.next = card_to_remove.next

        return True

    def get_list(self):
        """
        Method used to return a Python list composed of all Card in the Deck.

        Returns:
            - cards_list (list) : the list of all the Cards.
        """
        card = self.head

        # Initialize the list with the head inside at the first position
        cards_list = [card]

        # Go through all the Card by 'next' relation and add to the list
        while card.next:
            card = card.next
            cards_list.append(card)

        return cards_list

    def cut_all_next(self):
        """
        Method used to remove all the 'next' relation of Cards in the Deck.

        Returns:
            - (bool) : True.
        """

        cards_list = self.get_list()

        for card in cards_list:
            card.cut_next()

        return True

    def shuffle(self):
        """
        Method used to shuffle the Deck.

        Returns:
            - (bool) : True when the deck is shuffle.
        """

        # We get the list of all the Cards in Deck and we remove all 'next' relations.
        cards = self.get_list()
        self.cut_all_next()

        # Shuffle the Deck by random module.
        random.shuffle(cards)

        # Set the new head of the Deck.
        self.head = cards[0]

        # Re-build all the 'next' relations.
        for i in range(len(cards)-1):
            card = cards[i]
            card.next = cards[i+1]

        return True

    def draw(self):
        """
        Draw is an action that we can decompose in two times :
        - first we get the first Card of the Deck.
        - then we change the second Card to become the new first one.

        If draw in an empty Deck, return None.

        Returns:
            - top_card (Card |None) : return the drawn Card, could be None if the Deck is empty.
        """

        # Get the top Card (return it at the end).
        top_card = self.get_first_card()

        # Put this top Card out of the Deck by setting the second Card at the "new" top.
        self.head = self.get_card(index=1)

        # Broke the 'next' relation because once we draw a Card, the Card is not link to the Deck anymore. (use 'if top_card' in case of empty Deck, because NoneType has not cut_next()).
        if top_card:
            top_card.cut_next()

        return top_card

    def has_black_card(self):
        """
        Method used to check if there remains at least one black Card in the Deck.
        This method has a (O)n comlexity : stop when see the first black Card but go through all the n Cards if no black Card in the Deck.

        Returns:
            - (bool) : True if there is at least one black Card in the Deck, False otherwise.
        """

        # Get a list of all the Cards in the Deck
        cards = self.get_list()

        # Go through all these Cards to check for black color
        for card in cards:
            if card.is_black():
                return True
        return False

def get_standard_deck():
    """
    Function which create a Deck() instance, composed of 54 standard Cards.

    Returns:
        - D (Deck()) : the Deck composed of 54 Cards.
    """
    cards = []
    for suit in ['Diamonds', 'Spades', 'Hearts', 'Clubs']:
        for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            cards.append(Card(value=value, suits=suit))
    
    for i in range(2):
        cards.append(Card('Joker'))

    D = Deck()
    D.head = cards[0]
    print(len(cards))
    for i in range(len(cards)-1):
        card = cards[i]
        card.next = cards[i+1]

    return D

if __name__ == '__main__':
    C1 = Card('2', 'Spades')
    C2 = Card('K', 'Diamonds')
    C3 = Card('Q', 'Diamonds')

    C1.next = C2
    C2.next = C3

    D = Deck()
    D.head = C1

    print(D.draw())
    print(D.draw())
    print(D.draw())
    print(D.draw())
    print(D.draw())
    print(D.draw())