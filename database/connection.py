from sqlmodel import SQLModel, create_engine, Session
from models.events import Event, EventUpdate
from pydantic import BaseSettings, BaseModel
from typing import List, Optional, Any
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, Indexed, init_beanie, PydanticObjectId
from models.users import User
from models.events import Event

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
        await init_beanie(database=client.planner, document_models=[Event, User])

    class Config:
        env_file = ".env"


class Database:
    def __ini__(self, model):
        self.model = model

    async def save(self, Document) -> None:
        await document.create()
        return 
    
    async def get(self, id: str) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    async def get_all(self) -> List:
        docs = await self.model.find_all().to_list()
        if docs:
            return docs
        return False
    
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}

        update_query = {"$set": {
            field : value for field, value in des_body.items()
        }}

        doc = await self.get(doc_id)
        if not doc:
            return False
        
        await doc.update(update_query)
        return doc
    
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    