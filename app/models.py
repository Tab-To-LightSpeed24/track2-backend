from sqlalchemy import Boolean, Column, Integer, String, Date, Text, Enum as SQLAlchemyEnum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import enum

class StatusEnum(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(SQLAlchemyEnum(StatusEnum))
    priority = Column(SQLAlchemyEnum(PriorityEnum))
    due_date = Column(Date)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)

    owner = relationship("Employee", back_populates="tasks")