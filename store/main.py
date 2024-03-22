from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:root@postgresdb:5432/postgres"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class VideoGame(Base):
    __tablename__ = "videogames"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    platform = Column(String)
    model = Column(String)
    price = Column(Integer)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_game/")
def create_game(db: Session = Depends(get_db)):
    # Perform the operation to write to the database
    new_game = VideoGame(title="Sample Title", platform="Sample Platform", model="Sample Model", price=0)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return {"message": "New game created successfully"}

