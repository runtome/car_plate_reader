import os

# Camera
CAMERA_ID = 0  # webcam index

# Database
DB_PATH = "plates.db"

# Storage
SAVE_DIR = "plate_crops"
os.makedirs(SAVE_DIR, exist_ok=True)

# OCR
OCR_CONFIG = "--oem 3 --psm 7 -l tha+eng"
TESSERACT_PATH = r"/usr/bin/tesseract"  # update for Windows (e.g. r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# Motion detection
MOTION_THRESHOLD = 5000
