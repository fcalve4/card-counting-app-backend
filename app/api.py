import sys, io

from fastapi import APIRouter
from app.game.game import Game
router = APIRouter()

@router.get("/")
def root():

    # Create a Game instance
    game = Game()

    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Deal a card from the deck and update the running count
    game.game_loop_iteration()


    # Reset redirect
    sys.stdout = sys.__stdout__

    # Return the captured output for DEBUGGING PURPOSES
    # THIS WILL NOT WORK AT PRODUCTION SCALE
    # This will return the output of the game loop to the API response
    return {"message": "Game loop executed. Check server logs for output.",
            "output": captured_output.getvalue()}
    

