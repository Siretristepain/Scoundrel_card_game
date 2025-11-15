# ======================
# Implement Player class
# ======================

from cards import Card

class Player():

    def __init__(self, name: str=None, life:int=20, max_life: int=20, weapon:Card=None):
        self.name = name
        self.life = life
        self.max_life = max_life
        self.weapon = weapon

    def __repr__(self):
        """
        Method used to have a friendly view of the Player.

        Returns:
            - (str) : description of the Player.
        """
        return f"Player : {self.name}, {self.life}/{self.max_life} PV."

    def is_alive(self):
        """
        Method used to check is the Player is alive.

        Returns:
            - (bool) : True if yes, False otherwise.
        """
        return self.life > 0

    def get_damage(self, damage:int):
        """
        Method used to deals 'damage' damages to the Player.

        Args:
            - damage (int) : the quantity of damage that the Player have to takes.

        Returns:
            - self.life (int) : the Player's life after damages.
        """
        self.life -= damage
        return self.life

    def get_life(self, heal:int):
        """
        Method used to add 'heal' points to the Player's life.
        Takes the max_life Player in consideration to not heal beyond that limit.

        Args:
            - heal (int) : the quantity of heal that the Player have to gains.

        Returns:
            - self.life (int) : the Player's life after heal.
        """
        total_life = self.life + heal
        if total_life > self.max_life:
            self.life = self.max_life
        else:
            self.life += heal
        return self.life

    def interact(self, card: Card=None):
        """
        Method which allows to interact with a given Card.
        This method check the Card's suits according to the Card class properties and redirect to the good interaction method.

        The interaction methods are :
        - interact_with_monter (to fight a monster)
        - interact_with_potion (to get a heal potion)
        - interact_with_weapon (to equip a new weapon)
        """

        # Monster's logic
        if card.suits in Card.monsters_suits:
            return self.interact_with_monster(card)

        # Potion's logic
        elif card.suits in Card.potions_suits:
            return self.interact_with_potion(card)

        # Weapon's logic
        elif card.suits in Card.weapons_suits:
            return self.interact_with_weapon(card)

        else:
            print(f"There's an issue in the interaction with that Card : {card}.")

    def interact_with_monster(self, card: Card=None):
        self.life -= card.power
        return True

    def interact_with_potion(self, card: Card=None):
        self.life += card.power

        if self.life > self.max_life:
            self.life = self.max_life

        return True

    def interact_with_weapon(self, card: Card=None):
        """
        Method used to equip a new weapon to the Player.
        Be careful, if the method is called without weapon, it will throw the current weapon.

        TODO: This method has to be finished after the Weapon class will implement ?
        """
        self.weapon = card
        return True

if __name__ == '__main__':
    P = Player("Raphael", max_life=50)
    print(P)
    # print(P.is_alive())
    # print(P.get_damage(11))
    # print(P.get_life(80))

    C1 = Card('5', 'Diamonds')
    print(P.weapon)
    print(P.interact(C1))
    print(P.weapon)
