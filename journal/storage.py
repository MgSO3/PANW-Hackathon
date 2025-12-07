import json
import os

#Shortcuts made for reading, writing, and overwriting files
def read(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)
def write(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
def overwrite(path):
    write(path,[])


