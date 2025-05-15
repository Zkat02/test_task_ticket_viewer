from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import Ticket as TicketModel, Watcher as WatcherModel, StatusEnum
from app.db.session import get_db
from app.schemas.users import TicketCreate, Ticket, WatcherCreate, Watcher

router = APIRouter()


@router.post("/tickets", response_model=Ticket)
async def create_ticket(ticket: TicketCreate, db: AsyncSession = Depends(get_db)):
    db_ticket = TicketModel(**ticket.dict())
    db.add(db_ticket)
    await db.commit()
    await db.refresh(db_ticket)
    return db_ticket


@router.post("/watchers", response_model=Watcher)
async def add_watcher(watcher: WatcherCreate, db: AsyncSession = Depends(get_db)):
    db_watcher = WatcherModel(**watcher.dict())
    db.add(db_watcher)
    await db.commit()
    await db.refresh(db_watcher)
    return db_watcher


@router.patch("/tickets/{ticket_id}/status", response_model=Ticket)
async def update_ticket_status(ticket_id: int, status: StatusEnum, db: AsyncSession = Depends(get_db)):
    stmt = select(TicketModel).filter(TicketModel.id == ticket_id)
    result = await db.execute(stmt)
    db_ticket = result.scalar_one_or_none()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db_ticket.status = status
    await db.commit()
    await db.refresh(db_ticket)
    return db_ticket


@router.get("/tickets", response_model=list[Ticket])
async def get_tickets(status: StatusEnum = None, user_id: int = None,
                      watcher_id: int = None, db: AsyncSession = Depends(get_db)):
    query = select(TicketModel)
    if status:
        query = query.filter(TicketModel.status == status)
    if user_id:
        query = query.filter(TicketModel.user_id == user_id)
    if watcher_id:
        query = query.join(WatcherModel).filter(WatcherModel.user_id == watcher_id)

    result = await db.execute(query)
    tickets = result.scalars().all()
    return tickets
