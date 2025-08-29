import os
from dotenv import load_dotenv


load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_FROM_PHONE")
TO_NUMBER = os.getenv("TWILIO_TO_PHONE")
TO_WHATSAPP = f"whatsapp:{TO_NUMBER}"

print("ACCOUNT_SID:", ACCOUNT_SID)
print("AUTH_TOKEN:", AUTH_TOKEN)
print("TWILIO_NUMBER:", TWILIO_NUMBER)
print("TO_NUMBER:", TO_NUMBER)

ESP32_PORT = os.getenv("ESP32_PORT")
ESP32_BAUD = int(os.getenv("ESP32_BAUD"))


FIREBASE_SERVICE_ACCOUNT = os.getenv("FIREBASE_SERVICE_ACCOUNT")
FIREBASE_COLLECTION = os.getenv("FIREBASE_COLLECTION")


MODEL_PATH = os.getenv("MODEL_PATH")
CONFIDENCE = float(os.getenv("CONFIDENCE"))
IMG_SIZE = int(os.getenv("IMG_SIZE"))
DEVICE = os.getenv("DEVICE")
SNAPSHOT_COOLDOWN = int(os.getenv("SNAPSHOT_COOLDOWN"))
SIREN_DURATION = int(os.getenv("SIREN_DURATION"))
