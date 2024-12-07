import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DB_PATHS = {
    "users": DATA_DIR / "users.json",
    "employees": DATA_DIR / "employees.json",
    "departments": DATA_DIR / "departments.json"
}

def ensure_db_exists():
    """Ensure all database files exist."""
    DATA_DIR.mkdir(exist_ok=True)
    for db_path in DB_PATHS.values():
        if not db_path.exists():
            with open(db_path, 'w') as f:
                json.dump([], f)

def read_db(db_name: str):
    """Read data from JSON file."""
    with open(DB_PATHS[db_name], 'r') as f:
        return json.load(f)

def write_db(db_name: str, data: list):
    """Write data to JSON file."""
    with open(DB_PATHS[db_name], 'w') as f:
        json.dump(data, f, indent=2)