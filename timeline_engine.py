from collections import deque
import threading, time

TIMELINE = deque(maxlen=500)
lock = threading.Lock()

def log_event(msg):
    ts = time.strftime("%H:%M:%S")
    with lock:
        TIMELINE.append(f"[{ts}] {msg}")

def get_timeline():
    with lock:
        return list(TIMELINE)
