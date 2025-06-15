import sys, io
from fastapi.responses import StreamingResponse
import json
import time
from fastapi import APIRouter
from app.game.game import Game
router = APIRouter()

@router.get("/stream")
def stream_game():
    
    def game_stream():
        game = Game()
        for event in game.game_loop_iteration():
            # Yield each event as a JSON line
            yield json.dumps(event) + "\n"
            time.sleep(0.5)  # simulate delay

    return StreamingResponse(game_stream(), media_type="application/json")

