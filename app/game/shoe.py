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
    
class Shoe():
    """
    Represents a shoe of cards.
    """

    def __init__(self, num_decks):
        """
        Initialize the shoe with a list of cards.
        :param cards: List of card objects.
        """
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.cards *= num_decks

    def shuffle(self):
        """
        Shuffle the shoe of cards.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draw a card from the top of the shoe.
        :return: The top card or None if the shoe is empty.
        """
        if self.cards:
            return self.cards.pop()
        return None
    

