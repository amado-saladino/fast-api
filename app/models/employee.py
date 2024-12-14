from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    fullName: str
    departmentId: str
    position: str

class EmployeePatch(BaseModel):
    fullName: Optional[str] = None
    departmentId: Optional[str] = None
    position: Optional[str] = None

class Employee(EmployeeBase):
    id: str
    createdAt: datetime
