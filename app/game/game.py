from app.game.shoe import Shoe
class Game(): 
    def __init__(self):
        # Init running count to zero
        self.running_count = 0
        self.num_decks = 6  # Default number of decks in the shoe

        # Create a deck and shuffle it initially
        self.shoe = Shoe(self.num_decks)
        self.shoe.shuffle()

        

    def game_loop_iteration(self):
        # Check if the shoe needs to be reshuffled
        if len(self.shoe.cards) == 0:
            print("Reshuffling the shoe...")
            self.shoe = Shoe(self.num_decks)
            self.shoe.shuffle()
            self.running_count = 0
        else:
            """                # Await player next card input
            input("Press Enter to draw the next card (or type 'exit' to quit): ")
            # if user types exit, break the loop
            if input().strip().lower() == 'exit':
                loop_active = False
                print("Exiting the game.")
                break"""
            # Draw a card from the shoe
            card = self.shoe.draw_card()

            # Update the running count based on the card drawn
            if card.rank in ['2', '3', '4', '5', '6']:
                self.running_count += 1
            elif card.rank in ['10', 'Jack', 'Queen', 'King', 'Ace']:
                self.running_count -= 1
            # Print the drawn card and the current running count
            print(f"Card drawn: {card}, Running Count: {self.running_count}")
        