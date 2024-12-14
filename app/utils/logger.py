import logging
from datetime import datetime
from pathlib import Path

def setup_logger():
    # Create logs directory
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Create logger
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s\n%(message)s\n-------------------------------------\n"
    )

    # Create file handler
    current_time = datetime.now()
    log_file = logs_dir / f"log-{current_time.hour}-{current_time.day}-{current_time.month}-{current_time.year}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

# Add specific auth logging methods
def log_failed_login(username: str, reason: str):
    """
    Log failed login attempts with username and reason.
    
    Args:
        username (str): The username that failed to login
        reason (str): The reason for the login failure
    """
    logger.warning(
        f"Failed Login Attempt\nUsername: {username}\nReason: {reason}"
    )

def log_successful_login(username: str):
    """
    Log successful login attempts.
    
    Args:
        username (str): The username that successfully logged in
    """
    logger.info(
        f"Successful Login\nUsername: {username}"
    )