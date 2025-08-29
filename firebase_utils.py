import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

load_dotenv()

cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT", "firebase_credentials.json")
collection_name = os.getenv("FIREBASE_COLLECTION", "wildguard_events")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

def log_event(data: dict):
    """Log detection event to Firestore"""
    try:
        db.collection(collection_name).add(data)
        print("✅ Firebase log saved:", data)
    except Exception as e:
        print("❌ Firebase log failed:", e)
