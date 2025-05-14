import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
TEMP_DIR = tempfile.mkdtemp()
NUTRITION_DATA_PATH = os.path.join(TEMP_DIR, "nutrition_data")
os.makedirs(NUTRITION_DATA_PATH, exist_ok=True)
