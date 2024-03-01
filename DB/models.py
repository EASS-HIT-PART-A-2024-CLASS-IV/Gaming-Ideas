from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GamePrice(Base):
    __tablename__ = "game_prices"

    id = Column(Integer, primary_key=True, index=True)
    game = Column(String, index=True)
    platform = Column(String, index=True)
    edition = Column(String, index=True)
    price = Column(Integer)

    def to_dict(self):
        return {"game": self.game, "platform": self.platform, "edition": self.edition, "price": self.price}
