import os
import pygame
import threading

SOUND_MAP = {
    "elephant": os.path.join("assets", "fire cracker.mp3"),
    "monkey": os.path.join("assets", "dog_bark.mp3"),
}

DEFAULT_SOUND = os.path.join("assets", "default_alarm.mp3")

def _ensure_pygame():
    if not pygame.mixer.get_init():
        pygame.mixer.init()

def _play_in_background(path: str, duration_sec: int):
    _ensure_pygame()
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        threading.Timer(duration_sec, pygame.mixer.music.stop).start()
    except Exception as e:
        print(f"Error playing sound: {e}")

def play_deterrent(animal: str, duration_sec: int = 20):
    animal_key = (animal or "").strip().lower()
    path = SOUND_MAP.get(animal_key, DEFAULT_SOUND if os.path.exists(DEFAULT_SOUND) else None)

    if path is None:
        print(f"No sound mapped for '{animal_key}', skipping sound.")
        return

    print(f"Deterrent: {animal_key or 'unknown'} → {os.path.basename(path)} ({duration_sec}s)")
    threading.Thread(target=_play_in_background, args=(path, duration_sec), daemon=True).start()
