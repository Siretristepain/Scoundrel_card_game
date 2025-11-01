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
    

if __name__ == '__main__':
    C1 = Card('2', 'Spades')
    C2 = Card('K', 'Diamonds')

    C1.next = C2

    D = Deck()
    print(D.get_size())
    print(D.get_first_card())
    print(D.get_last_card())
