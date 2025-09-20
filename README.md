# 🚗 Thai License Plate Recognition System

This project is a **real-time license plate recognition (LPR) system** designed for Thai license plates.
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

## 📂 Project Structure
```bash
plate_reader/
│
├── main.py                # Entry point - starts all worker threads
├── config.py              # Central config (camera, db, OCR, thresholds)
├── db.py                  # Database setup and save functions
├── sort.py                # SORT tracker implementation
│
└── workers/               # Worker threads (modular pipeline)
    ├── capture_worker.py  # Capture frames from webcam
    ├── motion_worker.py   # Detect motion and filter frames
    ├── detector_worker.py # Run YOLO + SORT tracker
    ├── ocr_worker.py      # Perform OCR on detected plates
    ├── db_worker.py       # Save results to SQLite database
    └── display_worker.py  # Visualize video with boxes + text

```

## 🛠️ Modules Overview

**main.py**
- Initializes database and queues
- Starts all workers in separate threads
- Keeps system running

**config.py**
- Camera settings
- Database file path
- OCR settings (tha+eng for Thai plates)
- Thresholds for motion detection

**db.py**
- Initializes SQLite database (plates.db)
- Provides function save_to_db() for inserting recognized plates

**sort.py**
- Implements SORT (Simple Online Realtime Tracking)
- Assigns unique IDs to detected objects across frames

**workers/**
Each worker runs as a threaded module:
- capture_worker.py → Reads webcam frames
- motion_worker.py → Detects movement, filters idle frames
- detector_worker.py → YOLOv8 detection + SORT tracking
- ocr_worker.py → Tesseract OCR on cropped plate regions
- db_worker.py → Saves recognition results into DB
- display_worker.py → Displays video with bounding boxes + OCR text

## ⚡ Pipeline Workflow

1. Capture Worker → grabs frames from webcam
2. Motion Worker → checks if there’s movement
3. Detector Worker → YOLO detects plates + SORT assigns IDs
4. OCR Worker → Crops license plate and runs Tesseract OCR
5. DB Worker → Saves plate text, timestamp, and crop path into SQLite
6. Display Worker → Shows live video with detection boxes + plate text

## 📋 Example Database Entry

```bash
id | plate_text         | confidence | timestamp                  | track_id | image_path
---+--------------------+------------+----------------------------+----------+-----------------------
1  | 1กช-1651 กรุงเทพมหานคร | 0.90       | 2025-09-14T15:00:01.123Z | 5        | plate_crops/5_169.png

```

## 🚀 How to Run
1. Install dependencies:
```bash
pip install ultralytics opencv-python pytesseract
```
Also install **Tesseract OCR** on your system.

2. Start the system:
```bash
python main.py
```
3. Press **q** in the display window to quit.
```bash

```