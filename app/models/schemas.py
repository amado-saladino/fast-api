from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    fullName: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None

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

class DepartmentBase(BaseModel):
    name: str
    description: str

class DepartmentPatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Department(DepartmentBase):
    id: str
    createdAt: datetime