from ultralytics import YOLO
from sort import Sort
from datetime import datetime

# Load YOLO model (replace with your trained weights for Thai plates)
model = YOLO("yolov8n.pt")
tracker = Sort(max_age=10, min_hits=2, iou_threshold=0.3)

def detector_worker(detector_queue, ocr_queue, display_queue):
    while True:
        frame = detector_queue.get()
        results = model(frame, verbose=False)

        detections = []
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = float(box.conf.cpu().numpy())
                detections.append([x1, y1, x2, y2, conf])

        tracked = tracker.update(detections)

        # Send crops to OCR
        for det in tracked:
            x1, y1, x2, y2, track_id = map(int, det)
            crop = frame[y1:y2, x1:x2]
            if crop.size == 0:
                continue
            ts = datetime.utcnow().isoformat()
            ocr_queue.put((crop, track_id, ts, (x1, y1, x2, y2)))

        # Send frame + tracked boxes (without OCR yet) to display
        display_queue.put((frame.copy(), tracked, []))
