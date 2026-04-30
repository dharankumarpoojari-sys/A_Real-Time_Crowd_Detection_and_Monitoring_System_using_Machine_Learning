# 🎯 Real-Time People Counting using YOLOv8 + Flask

## 👨‍💻 Developed By

**Name:** Dharan Kumar Poojari
**Email:** [dharankumarpoojari@gmail.com](mailto:dharankumarpoojari@gmail.com)

---

## 📌 Project Overview

This project is a **web-based real-time people counting system** that processes uploaded videos and detects the number of people present using **YOLOv8**.

The application uses a Flask backend to handle video uploads and streams the processed video with bounding boxes and live people count.

---

## 🚀 Features

* 📤 Upload video through web interface
* 👥 Detect **multiple people** in each frame
* 🔢 Display **real-time people count**
* 🎥 Stream processed video live in browser
* ⚡ Fast detection using **YOLOv8 Nano model**

---

## 🧠 Technologies Used

* **Python**
* **Flask** (Web Framework)
* **OpenCV** (Video Processing)
* **YOLOv8 (Ultralytics)** (Object Detection)

---

## 📂 Project Structure

```
project/
│
├── app.py              # Main Flask application
├── static/
│   └── uploads/       # Uploaded videos
├── templates/
│   ├── index.html     # Upload page
│   └── result.html    # Output streaming page
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd project
```

### Step 2: Install Dependencies

```bash
pip install flask opencv-python ultralytics
```

### Step 3: Download YOLOv8 Model

```bash
yolo task=detect mode=predict model=yolov8n.pt source=0
```

---

## ▶️ How to Run

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

## 🎯 Usage

* Upload a video file
* The system processes each frame
* People are detected using YOLOv8
* Bounding boxes are drawn around each person
* Live count is displayed on the video

---

## 🧠 Model Info

* Model: **YOLOv8 Nano (`yolov8n.pt`)**
* Class used: **0 (Person Detection)**

---

## ⚠️ Notes

* Supports formats like **.mp4, .avi**
* Processing speed depends on system performance
* First run may download YOLO model automatically
* Ensure correct file path if video doesn't load

---

## 🔥 Future Enhancements

* 🎥 Live webcam integration
* 📊 Crowd density analytics dashboard
* 🚨 Alert system for overcrowding
* 💾 Database integration (MongoDB)
* ⚡ GPU acceleration support

---

## 📬 Contact

For queries, suggestions, or collaboration:

📧 **[dharankumarpoojari@gmail.com](mailto:dharankumarpoojari@gmail.com)**


