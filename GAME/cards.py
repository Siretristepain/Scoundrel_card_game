# ======================
# Implement Card() class
# ======================

from utils.cards_utils import powers, suits_emoji

class Card():

    def __init__(self, value=None, suits=None, power=None, next=None):
        self.value = value
        self.suits = suits
        power = powers.get(self.value, None)
        self.power = power

        # Link to the next Card
        self.next = next
        print(f"Card created : {self.value} of {self.suits}, power : {self.power}")

    def __repr__(self):
        """
        Méthod used to have a friendly representation of a Card when we do 'print(Card)'.
        """
        return f"{str(self.value)} {suits_emoji.get(self.suits, self.suits if self.value != 'Joker' else suits_emoji.get('Joker'))}"

    def is_null(self):
        """
        Method used to see if a card has no value.

        Returns:
            - (bool) : True if no value, False otherwise.
        """
        return self.value == None

    def is_face_card(self):
        """
        Méthod used to check if a Card is a face card.

        Returns:
            - (bool) : True if the card is a face card, False otherwise.
        """
        return self.value in ['J', 'Q', 'K']
    
    def is_eaven(self):
        """
        Method used to check if a card has a eaven value.
        Note : The method return False if the card is a face card.

        Returns:
            - (bool) : True if the value is eaven, False otherwise.
        """

        if self.is_face_card():
            return False
        
        return int(self.value) % 2 == 0
    
    def is_odd(self):
        """
        Method used to check if a card has an odd value.
        Note : The method return False if the card is a face card.

        Returns:    
            - (bool) : True is the value is odd, False, otherwise.
        """

        if self.is_face_card():
            return False
        
        return int(self.value) % 2 != 0
    
    def is_red(self):
        """
        Method used to check if a card has a red color (if his suits is Hearts or Diamonds).

        Returns:
            - (bool) : True if the card is red, False otherwise.
        """
        return self.suits in ['Hearts', 'Diamonds']
    
    def is_black(self):
        """
        Method used to check if a card is black (if his suits is Clubs or Spades).

        Returns:
            - (bool) : True if the card is black, False, otherwise.
        """
        return self.suits in ['Clubs', 'Spades']
    
    def is_joker(self):
        """
        Method used to check if the card is a Joker.

        Returns:
            - (bool) : True if the card is a Joker, False otherwise.
        """
        return self.value == 'Joker'
    
    def is_greater(self, other_card):
        """
        Method used to check if the current card has a greater power than the 'other_card'.

        Args:
            - other_card (Card()) : the card to compare power.

        Returns:
            - (bool) : True if the current card has a greater power, False otherwise.
        """
        return self.power > other_card.power
    
    def is_lower(self, other_card):
        """
        Method used to check if the current card has a lower power than the 'other_card'.

        Args:
            - other_card (Card()) : the card to compare power.

        Returns:
            - (bool) : True if the current card has a lower power, False otherwise.
        """
        return self.power < other_card.power
    
    def is_equal(self, other_card):
        """
        Method used to check if the current card has an equal power to the 'other_card'.

        Args:
            - other_card (Card()) : the card to compare power.

        Returns:
            - (bool) : True if the current card as an equal power, False otherwise.
        """
        return self.power == other_card.power

    def cut_next(self):
        """
        Method used to remove the 'next' pointer of the Card.

        Returns:
            - (bool) : True.
        """
        self.next = None

        return True

if __name__ == '__main__':
    C1 = Card('K', 'Clubs')
    C2 = Card('8', 'Diamonds')

    print(C2.is_greater(C1))
    print(C2.is_lower(C1))

def generate_standard_54_cards_deck():
    """
    Function used to create a "deck" of 54 standard cards.
    In this case, the "deck" is just a simple Python list of 54 instances of Card() class.

    Returns:
        - deck (list[Card()]) : list of the 54 Card objects.
    """

    # Simple list to represent the "deck"
    deck = []

    # Start by create the 52 standard cards
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
            deck.append(Card(value, suit))

    # Finish by create the 2 Jokers
    for i in range(2):
        deck.append(Card('Joker'))

    return deck

if __name__ == '__main__':
    deck = generate_standard_54_cards_deck()
    print(deck)
    print(len(deck)) # 54
