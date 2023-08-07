from beanie import Document
from typing import List, Optional

class Event(Document, table=True):
    id: int 
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://sh2orc.com",
                "description" : "We will be",
                "tags":["python", "fastapi","book","launch"],
                "location": "Google Meet",
            }
        }

    class Settings:
        name = "events"

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        schema_extra = {
            "example":{
                "title": "FastAPI Book Launch",
                "image": "https://sh2orc.com",
                "description" : "We will be",
                "tags":["python", "fastapi","book","launch"],
                "location": "Google Meet",
            }
        }