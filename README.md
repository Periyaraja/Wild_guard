# 🌱 WildGuard – AI + IoT Farm Protection System

WildGuard is a smart surveillance and alert system designed to protect farmlands from wild animal intrusions.
It combines AI-powered detection, IoT-based deterrents, and cloud-connected alerts to act as a 24/7 digital guard for farmers.

# 🚜 Problem Statement

Farmers face huge losses when wild animals like elephants, monkeys, or boars enter their fields.
Traditional fences, CCTV, or alarms often fail because:

They cannot identify what kind of animal is approaching.

They send too many false alerts.

They don’t provide real-time warnings to farmers.

WildGuard solves this by combining computer vision + IoT + cloud alerts in one powerful system.

# 🛠️ Features

✅ Real-time animal detection using YOLOv8
✅ Animal-specific deterrent sounds (e.g., firecrackers for elephants, dog barking for monkeys)
✅ WhatsApp & SMS alerts with snapshots
✅ ESP32 buzzer alarm for local deterrence (works even offline)
✅ Firebase Firestore cloud logging of all events
✅ Ignores humans to prevent false alarms
✅ Modular design → expandable to multiple cameras

# 🔧 Tech Stack

Python → Detection engine

YOLOv8 + OpenCV → Real-time video analysis

ESP32 → IoT buzzer alert system

Twilio API → SMS & WhatsApp notifications

Firebase Firestore → Cloud database for logging events

Pygame → Play deterrent sounds

# 📂 Project Structure
wildguard/
│── detection.py          # Main detection loop
│── alert.py              # Alert pipeline (sound, buzzer, sms, firebase)
│── sound.py              # Plays deterrent sounds
│── message.py            # Twilio SMS/WhatsApp functions
│── buzzer.py             # ESP32 buzzer trigger
│── firebase_utils.py     # Firebase Firestore logging
│── .env                  # Secrets (Twilio, Firebase config, ESP32 port)
│── assets/               # Alarm sounds (firecracker, dog bark, etc.)
│── snapshots/            # Auto-saved detection images

# ⚡ Installation
1. Clone this repo
git clone https://github.com/your-username/wildguard.git
cd wildguard

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables

Create a .env file in the root folder:

# Twilio
TWILIO_ACCOUNT_SID=xxxx
TWILIO_AUTH_TOKEN=xxxx
TWILIO_FROM_PHONE=+1415xxxx
TWILIO_TO_PHONE=+91xxxxxxxxxx

# ESP32
ESP32_PORT=COM5
ESP32_BAUD=115200

# Firebase
FIREBASE_SERVICE_ACCOUNT=./firebase_credentials.json
FIREBASE_COLLECTION=wildguard_events

# Detection
MODEL_PATH=yolov8n.pt
CONFIDENCE=0.35
IMG_SIZE=640
DEVICE=cpu
SNAPSHOT_COOLDOWN=8
SIREN_DURATION=20

5. Run detection
python detection.py

📡 System Architecture
graph TD;
    Camera --> Detection[YOLOv8 Detection Script]
    Detection -->|Deterrent Sound| Speaker
    Detection -->|Command| ESP32[Buzzer Alarm]
    Detection -->|Snapshot & Log| Firebase[Firestore Cloud]
    Detection -->|SMS/WhatsApp| Twilio[Twilio API]
    Firebase --> FarmerApp[Mobile Farmer Alerts]

# 📊 Example Output

Detected: Elephant (0.87 confidence)

Snapshot saved: snapshots/elephant_2025-08-23.jpg

Firebase log: Event stored with timestamp

Twilio alert: Farmer receives SMS/WhatsApp

# 🚀 Future Enhancements

GPS location tagging with alerts

Support for multiple farm cameras

Farmer dashboard with statistics

AI model fine-tuned for Indian wildlife

Solar-powered standalone version

# ❤️ Impact

WildGuard isn’t just a tech project – it’s a step towards:

Reducing crop damage

Protecting farmer livelihoods

Minimizing human-wildlife conflicts


