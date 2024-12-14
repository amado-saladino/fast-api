from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from ..utils.auth import (
    verify_password,
    hash_password as get_password_hash,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from ..config.database import read_db, write_db
from ..models.user import UserCreate, Token
from ..utils.logger import logger, log_failed_login, log_successful_login
import time

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    users = read_db("users")
    if any(existing_user["username"] == user.username for existing_user in users):
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(user.password)
    new_user = {
        "id": str(int(time.time() * 1000)),
        "username": user.username,
        "password": hashed_password,
        "fullName": user.fullName,
        "created_at": str(time.time())
    }

    users.append(new_user)
    write_db("users", users)
    logger.info(f"New user registered: {user.username}")
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    users = read_db("users")
    user = next((user for user in users if user["username"] == form_data.username), None)

    if not user or not verify_password(form_data.password, user["password"]):
        log_failed_login(form_data.username, "Invalid credentials")
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    log_successful_login(form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}