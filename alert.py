from sound import play_deterrent
from buzzer import trigger_buzzer
from message import send_sms, send_whatsapp
from firebase_utils import log_event
from datetime import datetime

def handle_alert(label, confidence, snapshot_path=None):
    print(f"ALERT: {label} detected with confidence {confidence:.2f}")

    play_deterrent(label, duration_sec=20)
    trigger_buzzer()

    message = f"WildGuard Alert: {label} detected ({confidence:.2f})."
    if snapshot_path:
        message += f" Snapshot saved: {snapshot_path}"

    try:
        send_sms(message)
    except Exception as e:
        print("SMS failed:", e)

    try:
        send_whatsapp(message)
    except Exception as e:
        print("WhatsApp failed:", e)

    try:
        log_event({
            "animal": label,
            "confidence": confidence,
            "time": datetime.now().isoformat(),
            "snapshot": snapshot_path
        })
    except Exception as e:
        print("Firebase log failed:", e)
