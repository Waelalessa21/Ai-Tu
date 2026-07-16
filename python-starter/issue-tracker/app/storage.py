from pathlib import Path 
import json


DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "issues.json"



def load():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save(issues):
    with open(DATA_FILE, "w") as f:
        json.dump(issues, f, indent = 2 )
        