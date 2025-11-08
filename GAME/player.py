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

    def equip_weapon(self, weapon: Card=None):
        """
        Method used to equip a new weapon to the Player.
        Be careful, if the method is called without weapon, it will throw the current weapon.

        TODO: This method has to be finished after the Weapon class will implement.
        """
        self.weapon = weapon
        return True

if __name__ == '__main__':
    P = Player("Raphael")
    print(P)
    # print(P.is_alive())
    print(P.get_damage(11))
    print(P.get_life(80))