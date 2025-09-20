import cv2

def display_worker(display_queue):
    frame_cache = None
    ocr_cache = []

    while True:
        frame, detections, ocr_results = display_queue.get()

        # Keep last frame if OCR result comes later
        if frame is not None:
            frame_cache = frame.copy()
            ocr_cache = []

            # Draw tracker boxes
            for det in detections:
                x1, y1, x2, y2, track_id = map(int, det)
                cv2.rectangle(frame_cache, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame_cache, f"ID {track_id}", (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        if ocr_results:
            ocr_cache.extend(ocr_results)

        # Draw OCR results on cached frame
        if frame_cache is not None:
            for res in ocr_cache:
                x1, y1, x2, y2 = res["bbox"]
                cv2.putText(frame_cache, res["plate_text"], (x1, y2 + 25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            cv2.imshow("License Plate Reader", frame_cache)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cv2.destroyAllWindows()
