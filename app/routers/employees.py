from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..utils.auth import get_current_user
from ..config.database import read_db, write_db
from ..models.employee import Employee, EmployeeBase, EmployeePatch
from ..utils.logger import logger
import time

router = APIRouter()

@router.get("", response_model=List[Employee])
async def get_employees(current_user: dict = Depends(get_current_user)):
    employees = read_db("employees")
    logger.info("Employees list retrieved")
    return employees

@router.post("")
async def create_employee(
    employee: EmployeeBase,
    current_user: dict = Depends(get_current_user)
):
    employees = read_db("employees")
    new_employee = {
        "id": str(int(time.time() * 1000)),
        **employee.dict(),
        "createdAt": str(time.time())
    }
    employees.append(new_employee)
    write_db("employees", employees)
    logger.info(f"New employee created: {employee.fullName}")
    return new_employee

@router.get("/current-user")
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    logger.info(f"Current user info retrieved: {current_user['fullName']}")
    return {"fullName": current_user["fullName"]}

@router.put("/{employee_id}")
async def update_employee(
    employee_id: str,
    employee_update: EmployeeBase,
    current_user: dict = Depends(get_current_user)
):
    employees = read_db("employees")
    employee_idx = next(
        (i for i, emp in enumerate(employees) if emp["id"] == employee_id),
        None
    )
    
    if employee_idx is None:
        raise HTTPException(status_code=404, detail="Employee not found")
        
    employees[employee_idx].update(employee_update.dict())
    write_db("employees", employees)
    logger.info(f"Employee updated: {employee_id}")
    return employees[employee_idx]

@router.patch("/{employee_id}")
async def patch_employee(
    employee_id: str,
    employee_update: EmployeePatch,
    current_user: dict = Depends(get_current_user)
):
    employees = read_db("employees")
    employee_idx = next(
        (i for i, emp in enumerate(employees) if emp["id"] == employee_id),
        None
    )
    
    if employee_idx is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    update_data = employee_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    employees[employee_idx].update(update_data)
    write_db("employees", employees)
    logger.info(f"Employee patched: {employee_id}")
    return employees[employee_idx]

@router.delete("/{employee_id}")
async def delete_employee(
    employee_id: str,
    current_user: dict = Depends(get_current_user)
):
    employees = read_db("employees")
    filtered_employees = [emp for emp in employees if emp["id"] != employee_id]
    
    if len(filtered_employees) == len(employees):
        raise HTTPException(status_code=404, detail="Employee not found")
        
    write_db("employees", filtered_employees)
    logger.info(f"Employee deleted: {employee_id}")
    return {"message": "Employee deleted successfully"}