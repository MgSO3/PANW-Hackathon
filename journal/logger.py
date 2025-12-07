#Logger for errors

import logging
import os

LOG = "journal.log"  

# Ensure the directory exists
log_dir = os.path.dirname(LOG)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)

# Create logger
logger = logging.getLogger("journal")
logger.setLevel(logging.INFO)
# File handler
fh = logging.FileHandler(LOG, encoding="utf-8")
fh.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# Add handlers
logger.addHandler(fh)
