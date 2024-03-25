from sqlalchemy import Column, Integer, String
from DB import Base

# Define database models
class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


