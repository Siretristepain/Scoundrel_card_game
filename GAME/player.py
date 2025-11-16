# ======================
# Implement Player class
# ======================

from cards import Card
from weapon import Weapon

class Player():

    def __init__(self, name: str=None, life:int=20, max_life: int=20, weapon: Weapon=None):
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
        """
        Method used to interact with a monster Card.
        If the Player has an equiped weapon, the method ask the Player's for defend.
        If he want to defend he lose life point equal to the difference between monster's power and weapon power.
        If he don't want to defend or the weapon can't defend or the Player don't have weapon he lose life point equal to the monster's power.

        Args:
            - card (Card) : the monster's Card which attack the Player.

        Returns:
            - (bool) : True when the interaction is over.
        """

        if self.weapon:
            # Maybe in futur it could be a better idea to dedicate an method to get Player's choice
            choice = input(f"Do you want to defend with your weapon ? (Y/n) : ")

            if choice.upper() == 'Y':
                if self.weapon.can_defend_on(card):
                    damage = card.power - self.weapon.power

                    if damage < 0:
                        damage = 0

                    self.get_damage(damage)
                    self.weapon.history.add_bottom_card(card)
                    return True
                else:
                    print(f"Your weapon can't defend on {card} because the last defended Card is {self.weapon.get_last_defended_card()}.")

        damage = card.power
        self.get_damage(damage)

        return True

    def interact_with_potion(self, card: Card=None):
        """
        Method used to interact with potion Card.
        When a Player do this, he gain life point equal to the potion's power, limited by the Player's max_life.

        Returns:
            - (bool) : True when the interaction is over.
        """
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

    C1 = Weapon('5', 'Diamonds')
    C2 = Card('8', 'Spades')
    print(P.weapon)
    print(P.interact(C1))
    print(P.weapon)

    print(P.interact(C2))
    print(P)
    print(P.weapon)
    print(type(P.weapon))
    print(P.weapon.get_last_defended_card())
