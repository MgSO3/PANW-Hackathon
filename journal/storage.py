import json
import os
from .logger import logger
#Shortcuts made for reading, writing, and overwriting files
def read(path):
    if not os.path.exists(path):
        logger.warning("File not found: %s", path)
        return []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
    except( json.JSONDecodeError, IOError) as e:
        logger.error("Failed to read file %s: %s", path, e)
def write(path, data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except( json.JSONDecodeError, IOError) as e:
        logger.error("Failed to write file %s: %s", path, e)
def overwrite(path):
    write(path,[])


