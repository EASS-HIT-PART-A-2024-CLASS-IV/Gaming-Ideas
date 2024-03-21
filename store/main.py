from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional
from sqlalchemy.orm import Session
from DB import models, DB

app = FastAPI()
db = DB()

class Game(str, Enum):
    fifa = "FIFA 24"
    cod = "Call of Duty: Warzone"
    LOL = "LOL"

class RequestBody(BaseModel):
    game: Game
    platform: str
    edition: str
@app.get("/")
def read_root():
    return {"message": "Welcome to the Gaming Store"}

@app.post("/get_game_price")
def get_game_price(request_data: RequestBody):
    with db.session_scope() as session:
        game = db.get_game_price(session, request_data.game, request_data.platform, request_data.edition)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        return game.to_dict()

