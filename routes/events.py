from beanie import PydanticObjectId
from fastapi import APIRouter, Body, Depends, HTTPException, status
from database.connection import Database

from models.events import Event, EventUpdate
from typing import List

event_database = Database(Event)

event_router = APIRouter(
    tags=["Events"],
)

events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if event:
        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied id does not exist"
    )

@event_router.post("/new")
async def create_new_event(new_event: Event) -> dict:
    
    await event_database.save(new_event)
    return {
        "message": "Event successfully created"
    }


@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
        return {
            "message": "Event successfully deleted"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied id does not exist"
    )