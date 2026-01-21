import time

EMAIL_COOLDOWN = 600   # 10 minutes
_last_alert = {}

def can_send(ip):
    now = time.time()
    if ip not in _last_alert or now - _last_alert[ip] > EMAIL_COOLDOWN:
        _last_alert[ip] = now
        return True
    return False
