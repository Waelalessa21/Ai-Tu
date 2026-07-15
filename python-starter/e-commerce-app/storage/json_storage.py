import json
from pathlib import Path
from .base import BaseStorage


class JsonStorage(BaseStorage):
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def get_all(self):
        if not self.file_path.exists() or self.file_path.stat().st_size == 0:
            return []
        with open(self.file_path, "r") as f:
            return json.load(f)

    def get_by_id(self, id):
        return next((item for item in self.get_all() if item["id"] == id), None)

    def create(self, data):
        items = self.get_all()
        items.append(data)
        with open(self.file_path, "w") as f:
            json.dump(items, f, indent=2)
