import sys, io
from fastapi.responses import StreamingResponse
import json
import time
from fastapi import APIRouter
from app.game.game import Game


router = APIRouter()

game = Game()

@router.get("/stream")
def stream_game():
    
    def game_stream():
        
        for event in game.game_loop_iteration():
            # Yield each event as a JSON line
            yield json.dumps(event) + "\n"
            time.sleep(0.5)  # simulate delay

    return StreamingResponse(game_stream(), media_type="application/json")

