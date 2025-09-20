# 🚗 Thai License Plate Recognition System

This project is a **real-time license plate recognition (LPR) system ** designed for Thai license plates.
It uses a webcam, a YOLO object detector, SORT tracker, and Tesseract OCR.

Plates and timestamps are stored in a SQLite database, and results are displayed live with bounding boxes and recognized plate text.

## 📌 Features
- Real-time video capture (webcam)
- Motion detection (only process frames when something moves)
- License plate detection using YOLOv8
- Multi-object tracking with SORT
- OCR using Tesseract (supports Thai + English)
- Save cropped plates and recognition results into SQLite
- Live visualization with bounding boxes and plate numbers