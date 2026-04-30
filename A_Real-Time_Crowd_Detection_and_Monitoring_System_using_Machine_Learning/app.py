import os
import cv2
from flask import Flask, render_template, Response, request, redirect, url_for
from ultralytics import YOLO

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLOv8 model (nano version - fast)
model = YOLO("yolov8n.pt")

video_path = None


def generate_frames():
    global video_path

    cap = cv2.VideoCapture(video_path)

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Run YOLO prediction
        results = model.predict(frame, conf=0.4, verbose=False)

        count = 0

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])

                # Class 0 = person
                if cls == 0:
                    count += 1

                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display Count
        cv2.putText(frame,
                    f'People Count: {count}',
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    global video_path

    file = request.files["video"]

    if file.filename == "":
        return "No selected file"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    video_path = filepath

    return redirect(url_for("result"))


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/video")
def video():
    return Response(generate_frames(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True)