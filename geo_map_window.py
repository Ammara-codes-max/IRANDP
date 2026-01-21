import os
import json
import webbrowser
from geo_mapper import locate_ip
from map_engine.map_connector import update_map

# =====================================================
# 🌍 OPEN LIVE GEO MAP WINDOW (FIXED HTTP MODE)
# =====================================================
def open_geo_window():
    try:
        # 🔥 VERY IMPORTANT FIX
        webbrowser.open_new_tab("http://localhost:8080/live_map.html")
    except Exception as e:
        print("Geo Map Open Error:", e)

# =====================================================
# 📍 ADD ATTACK POINT TO REAL MAP
# =====================================================
def add_point(ip):
    try:
        country, lat, lon = locate_ip(ip)

        # 🛡 fallback for private / unknown IPs
        if lat is None or lon is None:
            lat, lon = 30.3753, 69.3451
            country = "Local Network"

        print(f"[GEO] {ip} -> {country} ({lat},{lon})")   # DEBUG TRACE

        update_map(ip, country, lat, lon)

    except Exception as e:
        print("Geo Point Error:", e)
