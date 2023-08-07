from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"],
)

events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied id does not exist"
    )

@event_router.post("/new")
async def create_new_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message": "Event successfully created"
    }
