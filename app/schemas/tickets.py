from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from enum import Enum

class StatusEnum(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None

class TicketCreate(TicketBase):
    user_id: int

class TicketUpdateStatus(BaseModel):
    status: StatusEnum

class AddWatcher(BaseModel):
    user_id: int

class TicketOut(TicketBase):
    id: int
    status: StatusEnum
    user_id: int
    watcher_ids: List[int]

    model_config = ConfigDict(from_attributes=True)