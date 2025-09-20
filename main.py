import time
from queue import Queue
from threading import Thread

from config import *
from db import init_db
from workers.capture_worker import capture_worker
from workers.motion_worker import motion_worker
from workers.detector_worker import detector_worker
from workers.ocr_worker import ocr_worker
from workers.db_worker import db_worker
from workers.display_worker import display_worker

if __name__ == "__main__":
    init_db()

    # Queues
    frame_queue = Queue(maxsize=4)
    detector_queue = Queue(maxsize=4)
    ocr_queue = Queue(maxsize=8)
    db_queue = Queue(maxsize=32)
    display_queue = Queue(maxsize=4)

    # Start threads
    Thread(target=capture_worker, args=(frame_queue,), daemon=True).start()
    Thread(target=motion_worker, args=(frame_queue, detector_queue), daemon=True).start()
    Thread(target=detector_worker, args=(detector_queue, ocr_queue, display_queue), daemon=True).start()
    Thread(target=ocr_worker, args=(ocr_queue, db_queue, display_queue), daemon=True).start()
    Thread(target=db_worker, args=(db_queue,), daemon=True).start()
    Thread(target=display_worker, args=(display_queue,), daemon=True).start()

    print("System running. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)
