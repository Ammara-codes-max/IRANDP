import time
from collections import defaultdict

stats = defaultdict(lambda: {"start": time.time(), "count": 0})

WINDOW = 3
RATE_THRESHOLD = 10

def analyze_user(ip):
    s = stats[ip]
    s["count"] += 1
    now = time.time()

    if now - s["start"] >= WINDOW:
        rate = s["count"] / (now - s["start"])
        stats[ip] = {"start": now, "count": 0}

        if rate >= RATE_THRESHOLD:
            return {"ip": ip, "rate": int(rate)}
    return None
