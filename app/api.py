import sys, io
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse
import json
import time
from fastapi import APIRouter
from app.game.game import Game


router = APIRouter()

# Store game state in memory (reset per process)
session = {
    "game": None
}

@router.post("/start")
def start_game():
    session["game"] = Game()
    return JSONResponse(content={"message": "New game session started."})


@router.get("/stream")
def stream_game():
    game = session.get("game")
    if game is None:
        return JSONResponse(content={"error": "Game not started"}, status_code=400)

    def game_stream():
        for event in game.game_loop_iteration():
            yield json.dumps(event) + "\n"
            time.sleep(0.5)  # simulate delay

    return StreamingResponse(game_stream(), media_type="application/json")
