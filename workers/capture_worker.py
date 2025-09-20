import cv2
from config import CAMERA_ID

def capture_worker(frame_queue):
    cap = cv2.VideoCapture(CAMERA_ID)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame_queue.put(frame)
