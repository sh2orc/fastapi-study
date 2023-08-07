from sqlmodel import JSON, SQLModel, Field, Column
from pydantic import BaseModel
from typing import List, Optional

class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
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

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = Field(sa_column=Column(JSON))
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