import time

sessions = {}

def update_session(ip):
    now = time.time()
    if ip not in sessions:
        sessions[ip] = {"start": now, "last": now, "count": 1}
    else:
        sessions[ip]["last"] = now
        sessions[ip]["count"] += 1

def get_sessions():
    return sessions
