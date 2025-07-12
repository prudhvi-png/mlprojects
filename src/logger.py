import logging
import os
from datetime import datetime

# Step 1: Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create 'logs' directory if it doesn't exist
logs_path = os.path.join(os.getcwd(), 'logs')  # Only the directory
os.makedirs(logs_path, exist_ok=True)

# Step 3: Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


