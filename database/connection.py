from sqlmodel import SQLModel, create_engine, Session
from models.events import Event, EventUpdate
from pydantic import BaseSettings
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, Indexed, init_beanie

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False} 
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
        
class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def init_db(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.planner, document_models=[])

    class Config:
        env_file = ".env"