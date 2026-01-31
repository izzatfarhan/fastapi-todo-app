
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

#create location if this db on fastapi app
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
#postgresql://postgres:izzatfarhan123@localhost/TodoApplicationDatabase

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ensure the database does not operate auto, we have fully control on the db
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)

Base = declarative_base()
