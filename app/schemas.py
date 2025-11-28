from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date
from .models import StatusEnum, PriorityEnum

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.todo
    priority: PriorityEnum = PriorityEnum.medium
    due_date: Optional[date] = None
    employee_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: Optional[int] = None

    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    role: str
    email: EmailStr
    is_active: bool = True

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    due_date: Optional[date] = None
    employee_id: Optional[int] = None

class StatsOverview(BaseModel):
    total_tasks: int
    completed_tasks: int
    overdue_tasks: int
    unassigned_tasks: int