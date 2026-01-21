from datetime import datetime

def log_incident(ip, packets, risk, reason):
    with open("incidents.log","a") as f:
        f.write(f"{datetime.now()} | IP:{ip} | Packets:{packets} | Risk:{risk} | {reason}\n")
