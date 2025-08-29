import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_FROM_PHONE")   
TO_NUMBER = os.getenv("TWILIO_TO_PHONE")         
TO_WHATSAPP = f"whatsapp:{TO_NUMBER}"            


ACCOUNT_SID = "AC0db5df86c*********************"
AUTH_TOKEN = "324ad36f*********************"
TWILIO_NUMBER = "+14*********"   
TO_NUMBER = "+91***********"         
TO_WHATSAPP = f"whatsapp:{TO_NUMBER}" 

print("ACCOUNT_SID:", ACCOUNT_SID)
print("AUTH_TOKEN:", AUTH_TOKEN)
print("TWILIO_NUMBER:", TWILIO_NUMBER)
print("TO_NUMBER:", TO_NUMBER)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(message):
    """Send SMS via Twilio"""
    msg = client.messages.create(
        body=message,
        from_='+16**********',
        to=TO_NUMBER
    )
    print("SMS sent:", msg.sid)

def send_whatsapp(message):
    """Send WhatsApp alert via Twilio"""
    msg = client.messages.create(
        body=message,
        from_="whatsapp:" + TWILIO_NUMBER,
        to=TO_WHATSAPP
    )
    print("📩 WhatsApp sent:", msg.sid)
