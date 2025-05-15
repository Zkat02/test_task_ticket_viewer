from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)


class WatcherBase(BaseModel):
    ticket_id: int
    user_id: int


class WatcherCreate(WatcherBase):
    pass


class Watcher(WatcherBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
