from app.game.shoe import Shoe
class Game(): 
    def __init__(self):
        # Init running count to zero
        self.running_count = 0
        self.num_decks = 6  # Default number of decks in the shoe

        # Create a deck and shuffle it initially
        self.shoe = Shoe(self.num_decks)
        self.shoe.shuffle()

    def update_count(self, card):
        if card.rank in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif card.rank in ['10', 'Jack', 'Queen', 'King', 'Ace']:
            self.running_count -= 1
        

    def game_loop_iteration(self):
        # Check if the shoe needs to be reshuffled
        if len(self.shoe.cards) == 0:
            self.shoe = Shoe(self.num_decks)
            self.shoe.shuffle()
            self.running_count = 0
        else:
            # Draw a card from the shoe
            card = self.shoe.draw_card()

            # Update the running count based on the card drawn
            self.update_count(card)

            # Calculate the number of decks remaining
            decks_remaining = round(len(self.shoe.cards) / 52 * 2) / 2

            # Print the drawn card and the current running count
            yield {
                "card": str(card),
                "count": self.running_count,
                "cards_remaining": len(self.shoe.cards),
                "decks_remaining": decks_remaining
            }