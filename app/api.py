import sys, io

from fastapi import APIRouter
from app.game.game import Game
router = APIRouter()

@router.get("/")
def root():

    # Create a PokerGame instance with the table of players
    game = Game()

    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Play a hand of blackjack with the number of players dealt in
    game.game_loop()

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Return the captured output for DEBUGGING PURPOSES
    # THIS WILL NOT WORK AT PRODUCTION SCALE
    # This will return the output of the game loop to the API response
    return {
        "message": "Game loop executed.",
        "output": captured_output.getvalue()
    }
    

