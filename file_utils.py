import os
from config import NUTRITION_DATA_PATH
from utils.debug import debug_print

def handle_upload(change):
    for filename, content in change['new'].items():
        file_path = os.path.join(NUTRITION_DATA_PATH, filename)
        with open(file_path, 'wb') as f:
            f.write(content['content'])
        debug_print(f"Uploaded file: {file_path} ({len(content['content'])} bytes)")
    print(f"Uploaded {len(change['new'])} files to {NUTRITION_DATA_PATH}")
