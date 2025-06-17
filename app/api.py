import time
import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from app.game.game import Game

router = APIRouter()

# In-memory session
session = {
    "game": None,
    "num_decks": 6  # Default number of decks
}

# --- Models ---

class SettingsRequest(BaseModel):
    num_decks: int

# --- Routes ---

@router.post("/settings")
def update_settings(settings: SettingsRequest):
    session["num_decks"] = settings.num_decks
    print(f"Number of decks updated to: {settings.num_decks}")
    return {"message": "Number of decks updated"}

@router.post("/start")
def start_game():
    num_decks = session.get("num_decks", 6)
    session["game"] = Game(num_decks=num_decks)
    return JSONResponse(content={"message": f"New game started with {num_decks} decks."})

@router.get("/stream")
def stream_game():
    game = session.get("game")
    if game is None:
        return JSONResponse(content={"error": "Game not started"}, status_code=400)

    def game_stream():
        for event in game.game_loop_iteration():
            yield json.dumps(event) + "\n"
            time.sleep(0.5)

    return StreamingResponse(game_stream(), media_type="application/json")
