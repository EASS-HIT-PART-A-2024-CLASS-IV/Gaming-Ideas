from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from DB.DB import SessionLocal, Game 

app = FastAPI()

# Define a Pydantic model for the game data
class GameCreate(BaseModel):
    name: str

# API endpoint to add a new game
@app.post("/games/")
def create_game(game_data: GameCreate):
    db = SessionLocal()
    db_game = Game(name=game_data.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


