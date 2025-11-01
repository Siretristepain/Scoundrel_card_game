# ======================
# Implement Deck() class
# ======================

from cards import Card

class Deck():

    def __init__(self, head: Card = None):
        self.head = head

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
        if self.is_empty:
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

if __name__ == '__main__':
    C1 = Card('2', 'Spades')
    C2 = Card('K', 'Diamonds')
    C3 = Card('Q', 'Diamonds')

    C1.next = C2

    D = Deck()
    D.head = C1
    print(D.get_size())
    # print(D.get_first_card())
    # print(D.get_last_card())
    # print(D.get_card(2))
    print(D.have_in(C2))
    print(D.have_in(C3))
    print(D.add_top_card(C3))
    print(D.have_in(C3))
    print(D.get_size())

