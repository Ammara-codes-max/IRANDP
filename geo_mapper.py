import requests

def locate_ip(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = r.json()
        if "loc" in data:
            lat, lon = data["loc"].split(",")
            return data.get("country","NA"), float(lat), float(lon)
    except:
        pass
    return None, None, None
