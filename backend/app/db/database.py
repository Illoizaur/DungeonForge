import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv(dotenv_path='./.env')

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
