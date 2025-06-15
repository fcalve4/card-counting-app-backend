import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Card():
    """
    Represents a single playing card with a suit and a rank.
    """

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck():
    """
    Represents a deck of cards.
    """

    def __init__(self):
        """
        Initialize the deck with a list of cards.
        :param cards: List of card objects.
        """
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]


    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draw a card from the top of the deck.
        :return: The top card or None if the deck is empty.
        """
        if self.cards:
            return self.cards.pop()
        return None
