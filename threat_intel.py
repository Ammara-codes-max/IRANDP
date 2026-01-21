import requests

API_KEY = "9a43901cc8be5a6d15d56648decfc5e93991e7ce13f76cbe62a7e0579aa548e23bf55e8835d37eb6"

def lookup_ip(ip):
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        params = {"ipAddress": ip, "maxAgeInDays": 90}
        headers = {"Accept": "application/json", "Key": API_KEY}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if r.status_code != 200:
            return {"error": f"API Error {r.status_code}"}
        return r.json()["data"]
    except Exception as e:
        return {"error": str(e)}
