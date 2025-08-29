import serial
import time
import os
from dotenv import load_dotenv

load_dotenv()

ESP32_PORT = os.getenv("ESP32_PORT", "COM10")
BAUD_RATE = 9600

def trigger_buzzer():
    """
    Sends a simple trigger command to ESP32 to activate the buzzer.
    """
    try:
        with serial.Serial(ESP32_PORT, BAUD_RATE, timeout=1) as ser:
            time.sleep(2)
            command = "BUZZ\n"
            ser.write(command.encode())
            print("Buzzer triggered")
    except Exception as e:
        print(f"Error connecting to ESP32: {e}")
