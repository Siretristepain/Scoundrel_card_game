# ======================
# Implement Weapon class
# ======================

from cards import Card
from deck import Deck

class Weapon(Card):

    def __init__(self, value=None, suits=None, power=None, next=None, history: Deck=Deck()):
        """
        A weapon is a standard Card instance, the only difference is that a weapon have an history of previous defended Card.
        This history can be represented as a linked list, as a Deck instance. A weapon can only defend on a Card with lower power than the last Card it's defends of.
        """
        Card.__init__(self, value, suits, power, next)
        self.history = history

    def is_valid_weapon(self):
        """
        Method used to check if a Card is a valid weapon.
        Weapons are identified by their suits, so a valid weapon is a Card which the suits is in weapon_suits (-> Card class propertie).

        Returns:
            - (bool) : True if valid weapon, False otherwise.
        """
        return self.suits in Card.weapons_suits

    def get_last_defended_card(self):
        """
        Method to get the last Card on which the current weapon have defended of.

        Returns:
            - (Card) : the last Card on which the current weapon have defended. Could be None if the weapon is not used again.
        """
        return self.history.get_last_card()

    def can_defend_on(self, card: Card):
        """
        Method to check if the current weapon can defend on the Card which attack.
        To check that, the method compare the last defended Card by the Weapon with the incoming attacking Card.

        Returns:
            - (bool) : True if the weapon can defend, False otherwise.
        """
        if card.is_lower(self.get_last_defended_card()):
            return True
        return False


if __name__ == '__main__':
    # On crée une arme 3 de carreaux qui a déjà défendu sur un 5 de piques.
    already_defended_card = Card('5', 'Spades')
    deck = Deck(head=already_defended_card) # !! Issue when we defined an empty head !!
    W = Weapon(value='3', suits='Diamonds', history=deck)

    # On regarde quelle est la dernière carte défendu par l'arme (normalement le 5 de piques)
    print(W.get_last_defended_card())

    # On créer un nouvel attaquant 6 de trèfles et on voit si l'arme peut défendre dessus (normalement non)
    card_attack_1 = Card('6', 'Clubs')
    print(W.can_defend_on(card_attack_1))

    # On créer un nouvel attaquant 4 de piques et on voit si l'arme peut défendre dessus (normalement oui)
    card_attack_2 = Card('4', 'Spades')
    print(W.can_defend_on(card_attack_2))
    print(W.is_valid_weapon())
    # Weapon.weapon_suits.append('Clubs')
    # print(W.is_valid_weapon())
