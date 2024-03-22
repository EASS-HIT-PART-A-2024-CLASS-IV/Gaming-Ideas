from sqlalchemy import Column, Integer, String
from DB.DB import Base

class VideoGame(Base):
    __tablename__ = "video_games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    platform = Column(String)
    model = Column(String)
    price = Column(Integer)
