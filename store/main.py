from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# SQLAlchemy setup
DATABASE_URL = "postgresql://postgres:root@postgresdb:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI setup
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database models
class VideoGame(Base):
    __tablename__ = "videogames"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    platform = Column(String)
    model = Column(String)
    price = Column(Integer)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request body
class Game(BaseModel):
    title: str = Field(min_length=1)
    platform: str = Field(min_length=1)
    model: str = Field(min_length=1)
    price: int

# FastAPI endpoints
@app.post("/create_game/")
def create_game(game: Game, db: Session = Depends(get_db)):
    new_game = VideoGame(title=game.title, platform=game.platform, model=game.model, price=game.price)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return {"message": "New game created successfully"}

# Example of returning HTML with Jinja2Templates
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    games = db.query(VideoGame).all()
    return templates.TemplateResponse("index.html", {"request": request, "games": games})


