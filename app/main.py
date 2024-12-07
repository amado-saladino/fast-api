from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .config.database import ensure_db_exists
from .utils.logger import logger
from .routers import health, auth, employees, departments

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Application starting up...')
    ensure_db_exists()
    logger.info("Database initialized")
    yield
    print('Application is shutting down...')

app = FastAPI(lifespan=lifespan)

@app.get('/', description="this is a sample GET method", name="root path")
async def root():
    return {
        "message": "Welcome to FastAPI!!",
        "version": 2.0
    }

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
