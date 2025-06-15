import json
from pathlib import Path

def load_user_data_from_file(file_path: str) -> dict:
    path = Path(file_path)
    with path.open() as f:
        return json.load(f)