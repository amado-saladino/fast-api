from fastapi import APIRouter
from ..utils.logger import logger

router = APIRouter()

@router.get("")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "OK"}