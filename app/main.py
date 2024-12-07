from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config.database import ensure_db_exists
from .utils.logger import logger
from .routers import health, auth, employees, departments

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(departments.router, prefix="/departments", tags=["departments"])

@app.on_event("startup")
async def startup_event():
    ensure_db_exists()
    logger.info("Database initialized")