from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from models import Base, GamePrice

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/my_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def session_scope():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class DB:
    def get_game_price(self, session: Session, game: str, platform: str, edition: str) -> GamePrice:
        return session.query(GamePrice).filter_by(game=game, platform=platform, edition=edition).first()

