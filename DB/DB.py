from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres:root@postgresdb:5432/postgres"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)