from config import DEBUG

def debug_print(*args):
    if DEBUG:
        print("[DEBUG]:", *args)
