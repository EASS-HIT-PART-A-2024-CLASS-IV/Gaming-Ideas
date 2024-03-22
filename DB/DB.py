from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the connection URL for PostgreSQL
DATABASE_URL = "postgresql://postgres:root@postgresdb:5432/postgres"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker to create sessions with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Function to create all tables in the database if they don't exist
def create_tables():
    Base.metadata.create_all(bind=engine)
