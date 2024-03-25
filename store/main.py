from fastapi import FastAPI
from DB.DB import SessionLocal, Game

app = FastAPI()

# API endpoint to add a new game
@app.post("/games/")
def create_game(name: str):
    db = SessionLocal()
    db_game = Game(name=name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
