from firebase_utils import log_event

event = {
    "animal": "test_animal",
    "confidence": 0.99,
    "time": "2025-08-23T12:00:00",
    "snapshot": None
}

print("🚀 Sending test event to Firestore...")
log_event(event)
