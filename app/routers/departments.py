from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..utils.auth import get_current_user
from ..config.database import read_db, write_db
from ..models.schemas import Department, DepartmentBase, DepartmentPatch
from ..utils.logger import logger
import time

router = APIRouter()

@router.get("", response_model=List[Department])
async def get_departments(current_user: dict = Depends(get_current_user)):
    departments = read_db("departments")
    logger.info("Departments list retrieved")
    return departments

@router.post("")
async def create_department(
    department: DepartmentBase,
    current_user: dict = Depends(get_current_user)
):
    departments = read_db("departments")
    new_department = {
        "id": str(int(time.time() * 1000)),
        **department.model_dump(),
        "createdAt": str(time.time())
    }
    departments.append(new_department)
    write_db("departments", departments)
    logger.info(f"New department created: {department.name}")
    return new_department

@router.put("/{department_id}")
async def update_department(
    department_id: str,
    department_update: DepartmentBase,
    current_user: dict = Depends(get_current_user)
):
    departments = read_db("departments")
    department_idx = next(
        (i for i, dept in enumerate(departments) if dept["id"] == department_id),
        None
    )
    
    if department_idx is None:
        raise HTTPException(status_code=404, detail="Department not found")
        
    departments[department_idx].update(department_update.dict())
    write_db("departments", departments)
    logger.info(f"Department updated: {department_id}")
    return departments[department_idx]

@router.patch("/{department_id}")
async def patch_department(
    department_id: str,
    department_update: DepartmentPatch,
    current_user: dict = Depends(get_current_user)
):
    departments = read_db("departments")
    department_idx = next(
        (i for i, dept in enumerate(departments) if dept["id"] == department_id),
        None
    )
    
    if department_idx is None:
        raise HTTPException(status_code=404, detail="Department not found")
    
    update_data = department_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    departments[department_idx].update(update_data)
    write_db("departments", departments)
    logger.info(f"Department patched: {department_id}")
    return departments[department_idx]

@router.delete("/{department_id}")
async def delete_department(
    department_id: str,
    current_user: dict = Depends(get_current_user)
):
    departments = read_db("departments")
    filtered_departments = [dept for dept in departments if dept["id"] != department_id]
    
    if len(filtered_departments) == len(departments):
        raise HTTPException(status_code=404, detail="Department not found")
        
    write_db("departments", filtered_departments)
    logger.info(f"Department deleted: {department_id}")
    return {"message": "Department deleted successfully"}