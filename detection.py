import cv2
import os
from ultralytics import YOLO
from datetime import datetime

from sound import play_deterrent
from alert import handle_alert

MODEL_PATH = "yolov8n.pt"
CONF_THRESHOLD = 0.6
SIREN_DURATION_SEC = 20

FOREST_FARM_ANIMALS = [
    "elephant", "bear", "zebra", "giraffe", "cow", "horse", "sheep"
]

def run_detection():
    print(f"Loading model: {MODEL_PATH} on cpu")
    model = YOLO(MODEL_PATH)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not found")
        return

    print("Camera started... press 'q' to quit")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = model.predict(frame, conf=CONF_THRESHOLD, verbose=False)

            for r in results:
                boxes = r.boxes
                for box in boxes:
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    label = model.names[cls]

                    if label not in FOREST_FARM_ANIMALS:
                        continue

                    xyxy = box.xyxy[0].cpu().numpy().astype(int)
                    cv2.rectangle(frame, (xyxy[0], xyxy[1]), (xyxy[2], xyxy[3]), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label} {conf:.2f}", (xyxy[0], xyxy[1] - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                    print(f"Detected crop intruder: {label} ({conf:.2f})")

                    os.makedirs("snapshots", exist_ok=True)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"snapshots/{label}_{timestamp}.jpg"
                    cv2.imwrite(filename, frame)
                    print(f"Snapshot saved: {filename}")

                    play_deterrent(label, duration_sec=SIREN_DURATION_SEC)
                    handle_alert(label, conf, snapshot_path=filename)

            cv2.imshow("WildGuard Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("Detection stopped")
                break

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    run_detection()
