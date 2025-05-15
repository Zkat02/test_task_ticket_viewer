from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class StatusEnum(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.OPEN
    user_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True

class WatcherBase(BaseModel):
    ticket_id: int
    user_id: int

class WatcherCreate(WatcherBase):
    pass

class Watcher(WatcherBase):
    id: int

    class Config:
        orm_mode = True
