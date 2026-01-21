import json
import os

DATA_FILE = "map_engine/live_data.json"

def update_map(ip, country, lat, lon):
    data = []

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.append({
        "ip": ip,
        "country": country,
        "lat": lat,
        "lon": lon
    })

    # keep only last 50 points
    data = data[-50:]

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
