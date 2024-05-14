import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_hand(self, deck, num_cards):
        for _ in range(num_cards):
            self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            print(f"{card.rank} of {card.suit}")

# Main game logic
def play_poker():
    deck = Deck()
    deck.shuffle()

    player = Player("Player 1")
    player.draw_hand(deck, 5)
    player.show_hand()

play_poker()