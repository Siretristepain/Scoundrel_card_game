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
