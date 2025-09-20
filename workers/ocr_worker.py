import cv2
import pytesseract
import time
from config import OCR_CONFIG, SAVE_DIR, TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def ocr_worker(ocr_queue, db_queue, display_queue):
    while True:
        crop, track_id, ts, bbox = ocr_queue.get()
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        text = pytesseract.image_to_string(gray, config=OCR_CONFIG)
        text = text.strip().replace("\n", " ")

        filename = f"{SAVE_DIR}/{track_id}_{int(time.time())}.jpg"
        cv2.imwrite(filename, crop)

        result = {
            "plate_text": text,
            "confidence": 0.9,
            "timestamp": ts,
            "track_id": int(track_id),
            "image_path": filename,
            "bbox": bbox
        }

        db_queue.put(result)
        display_queue.put((None, [], [result]))  # send OCR results for overlay
