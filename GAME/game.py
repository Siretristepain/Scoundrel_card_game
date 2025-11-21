# ==============
# Implement game
# ==============

# Import
from board import Board
from cards import Card
from deck import Deck, get_standard_deck
from player import Player
from weapon import Weapon

# Function to create appropriate deck
def create_deck():
    cards = []
    black_values = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    red_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

    for black_suits in ['Spades', 'Clubs']:
        for value in black_values:
            cards.append(Card(value=value, suits=black_suits))
    
    for red_suits in ['Hearts', 'Diamonds']:
        for value in red_values:
            cards.append(Card(value=value, suits=red_suits))

    D = Deck()
    D.head = cards[0]
    for i in range(len(cards)-1):
        card = cards[i]
        card.next = cards[i+1]

    return D


# Deck creation
deck = create_deck()
print(deck.get_size())

# Shuffle the Deck
deck.shuffle()

# Discard pile
discard = Deck()

# Player creation
player_name = input("Player's name : ")
player = Player(name=player_name, life=20, max_life=20)

# Board creation
board = Board(
    player=player,
    deck=deck,
    discard=discard,
)

# Constants
quit = False
turns = 1
pass_previous_room = False

# Game Loop
while board.check_victory() == False and board.check_defeat() == False and quit == False:

    # Show room
    board.get_room()
    print(board)

    # Ask for Player's choice
    if pass_previous_room == False:
        choice = input(f"Enter or pass ? (E/p) ")

        if choice.upper() == 'P':
            pass_previous_room = True

    else:
        # Mandatory to enter
        choice = 'E'

    if choice.upper() == 'E':
        number_of_interaction = 1

        while number_of_interaction < 4:
            index_of_card_to_interact = int(input(f"With which Card would you interact ? (1/2/3/4) : "))
            
            if index_of_card_to_interact == 1:
                if board.slot_1 == None:
                    continue
                player.interact(board.slot_1)
                board.slot_1 = None
                print(board)
            elif index_of_card_to_interact == 2:
                if board.slot_2 == None:
                    continue
                player.interact(board.slot_2)
                board.slot_2 = None
                print(board)
            elif index_of_card_to_interact == 3:
                if board.slot_3 == None:
                    continue
                player.interact(board.slot_3)
                board.slot_3 = None
                print(board)
            elif index_of_card_to_interact == 4:
                if board.slot_4 == None:
                    continue
                player.interact(board.slot_4)
                board.slot_4 = None
                print(board)
            else:
                print(f"Error with indexed Card to interact with.")
            
            number_of_interaction += 1
        
        # Set pass_previous_room on False (because if the Player enter a room, he can pass the next one).
        pass_previous_room = False

    
print("=== Fin du jeu ===")
