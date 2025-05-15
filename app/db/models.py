import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base


class StatusEnum(str, enum.Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.OPEN)
    user_id = Column(Integer, nullable=False)

    watchers = relationship("Watcher", back_populates="ticket", lazy="selectin")


class Watcher(Base):
    __tablename__ = "watchers"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    user_id = Column(Integer)

    ticket = relationship("Ticket", back_populates="watchers", lazy="selectin")
