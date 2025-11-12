# Scoundrel_card_game
A Python version of the Scoundrel card game.

## What's Scoundrel ?

Scoundrel is a card game in which the player takes on the role of an adventurer who must traverse a dungeon.
The game is played with a standard 54-card deck. The rules are explain in details below.

TO DO: explain rules.

## How implement the game ?

Here is the current status of the project :

| Class | Card | Deck | Weapon | Player | Board |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Class Properties | ----- | ----- | weapon_suits | ----- | ----- |
| Instance Properties | value, suits, power, next | head | value, suits, power, next, history | name, life, max_life, weapon | deck, discard, slot_1, slot_2, slot_3, slot_4, weapon |
| Methods | \_\_repr__, is_null, is_face_card, is_eaven, is_odd, is_red, is_black, is_joker, is_greater, is_lower, is_equal, cut_next | \_\_repr__, is_empty, get_size, get_first_card, get_last_card, get_card, have_in, add_top_card, add_bottom_card, add_card, get_index, remove_card, get_list, cut_all_next, shuffle, draw | is_valid_weapon, get_last_defended_card, can_defend_on | \_\_repr__, is_alive, get_damage, get_life, equip_weapon | \_\_repr__, get_room, clear_slots, pass_room |

To do (in French):

Le jeu va tourner dans une boucle while.
Il faut donc définir les conditions d'arrêt :
- la vie du Player est inférieure ou égale à 0 (--> perdu)
- il n'y a plus aucun monstre dans le Deck et sur le Board (--> victoire)
- le Player décide de quitter la partie en cours (--> quit)

Pour identifier la victoire, je pense donc qu'il va falloir créer une méthode dans Deck pour voir s'il reste des cartes noires dans le Deck.
De plus, dans Board, il faudra faire la même chose.
Si aucun carte noire ni sur le Board, ni dans le Deck, alors Victoire!

Il va falloir créer un nouveau fichier game.py .
Dans ce fichier, il faudra importer toutes les classes : Card, Deck, Weapon, Player, Board.
C'est dans ce fichier que je vais implémenter la logique du jeu (la boucle while).
C'est dans ce fichier qu'on ira chercher les inputs du joueur.

- Créer un deck de 44 cartes (standard, sans tête rouges ni As rouges, ni Joker).
- Demander son nom au joueur.
- Créer un joueur avec ce nom (Player).
- Créer un Board et lui attacher le deck et le joueur.
- Créer un booléen 'quit' sur False.
- Créer une variable turns = 0
- Créer un booléen 'pass_previous_room' sur False

- Démarrer la boucle while avec les conditions d'arrêts.
- Si turns == 0, afficher une room directement
- Si turns != 0:
    - Si 'pass_previous_room' == True:
        - afficher une nouvelle room entièrement
    - Si 'pass_previous_room' == False:
        - ça veut dire qu'il reste une carte sur le plateau et qu'on ne veut pas afficher une nouvelle room entière mais juste compléter de 3 cartes l'existante (créer une méthode spéciale fill_room() ?)

- Proposer d'entrer ou de passer la room.
- Si passer, alors mettre 'pass_previous_room' sur True

- Si entrer :
    - Demander au joueur avec quelle carte intéragir (1, 2, 3 ou 4)
    - Faire l'effet de la carte.
    - Répéter cela 3 fois.
    - Il reste donc 1 carte sur le Board.
    - remettre 'pass_previous_room' sur False (il peut déjà l'être mais il peut aussi être sur True donc bon).


Table of methods to implement :

| Method name | argument | Class | Notes | Done |
| ----- | ----- | ----- | ----- | ----- |
| has_black_card | self | Deck | return True if remains at least one black Cards in the Deck, False otherwise (we can stop the search at the first black card found). | ----- |
| black_card_on_board | self | Board | return True if there is at leat one black Card on Board, False otherwise. | ----- |
| check_victory | self, deck | Board | return (not deck.has_black_card) & (not black_card_on_board) (True only when the two are False). | ----- |
| check_defeat | self, player | Board | return not player.is_alive (so I have to link the Player to the Board) --> check_defeat returns True when the Player lose. | ----- |
| interact_with_monster | self | Card | suppose that we previously check that the 'self' is a monster. Deals damage equal to monster's power to the Player by calling get_damage method.  | ----- |
| interact_with_weapon | self | Card | suppose that we previously check that 'self' if a weapon. Equip the new weapon to the Player by calling equip_weapon.| ----- |
| interact_with_potion | self | Card | suppose that we previously check that 'self' is a potion. Add potion's value to the Player's life (according to max_life) by calling get_life (rename get_life by add_life ?). | ----- |
| interact | self | Card | method that check the "type" of the Card and then call the good interact method | ----- |
| fill_room | self | Board | Complete a room with 3 new Cards after the Player enter the previous one (this method is used when it still 1 Card on the Board and we want to show a new room). | ----- |

Table of posibilities to explains check_victory logic :

| deck.has_black_card | black_card_on_board | check_victory |
| ----- | ----- | ----- |
| False | False | **True** |
| True | False | False |
| False | True | False |
| True | True | False |