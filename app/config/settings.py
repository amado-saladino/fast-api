import json
from pathlib import Path
from typing import Dict, Any

def load_config()-> Dict[str, Any]:
    """
    Load configuration from config.json file.
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

config = load_config()