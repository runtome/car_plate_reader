import cv2
from config import MOTION_THRESHOLD

def motion_worker(frame_queue, detector_queue):
    prev = None
    while True:
        frame = frame_queue.get()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small = cv2.resize(gray, (320, 240))
        if prev is None:
            prev = small
            continue
        diff = cv2.absdiff(prev, small)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        motion = cv2.countNonZero(thresh)
        if motion > MOTION_THRESHOLD:
            detector_queue.put(frame)
        prev = small
