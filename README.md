# Scoundrel_card_game
A Python version of the Scoundrel card game.

## What's Scoundrel ?

Scoundrel is a card game in which the player takes on the role of an adventurer who must traverse a dungeon.
The game is played with a standard 54-card deck. The rules are explain in details below.

TO DO: explain rules.

## How implement the game ?

The first of all thing is to create a standard deck. We will discuss the game logic in a second time.
We can imagine a deck as a linked list (chained list?). As a reminder, a linked list is a list composed of several nodes. Each node has his own value and a pointer to the next node. A linked list can be visualized as a necklace chain. If you look closely, the chain is made up of several links. In this example, the necklace chain is the linked list and each links is a node. If you take the first links, you will grab all the necklace chain.

So, we have to create a class to represente Card (-> Node) and a class to represent Deck (Linked List). We will discuss these classes :

**Card** :
A Card is define by several properties : value (2, 3, ..., J, Q, K, A, Joker), suits (Hearts, Diamonds, Clubs, Spades), power ?

Here is some interesting methods to implement in the Card logic :
- Is a face card ?
- Is eaven / Is odd ?
- Has red color ? Has black color ?
- Is greater than ... ?
- Is lower than ... ?
- Is a joker ?

**Deck** :
As we said, a Deck is a linked chain. So, it's define by a "head". This is the first node (-> the first card).

Here is some interesting methods to implement in the Deck logic :
- Is empty ?
- Get size of the deck.
- Get first card of the deck.
- Get last card of the deck.
- What's the card at the index i in the deck?
- Does the X card is in the deck?
- Add a X card at the begining of the deck (top of the deck).
- Add a X card at the bottom of the deck.
- Add a X card at the i position of the deck.
- Remove the X card in the deck.
- suffle the deck.
- draw the first card of the deck. (--> same as get first card ?)
- get index of a given Card in the Deck ?

**Board** :
I think that the best idea is to create a class for the board game. Thanks to that, it will be simple to show rooms during the game.
The board need to have 5 Cards slots : 4 for the room's Cards and one for the potential equiped weapon.

**Discard pile** :
As the board, I think the best idea is to create a class for the discard pile ? Maybe it's juste a Deck instance ??
