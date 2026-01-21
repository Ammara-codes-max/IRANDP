import pickle, subprocess, pandas as pd, time
from incident_logger import log_incident
from attack_classifier import classify_attack
from risk_trend import add_risk
from session_tracker import update_session
from threat_meter import add_risk as meter_add_risk
from attack_stats import update_attack

DEMO_MODE = True

# ---- Load AI model ----
with open("ai_model.pkl","rb") as f:
    model = pickle.load(f)

blocked_ips = set()
last_counts = {}
last_times = {}
baseline_packets = {}
START_TIME = time.time()
WARMUP = 30   # seconds learning phase

def analyze_and_contain(ip, packet_count):
    now = time.time()
    update_session(ip)

    # ---- Build baseline first ----
    baseline_packets[ip] = baseline_packets.get(ip, []) + [packet_count]
    if len(baseline_packets[ip]) > 10:
        baseline_packets[ip].pop(0)

    # ---- No alerts during warmup ----
    if time.time() - START_TIME < WARMUP:
        return

    prev_c = last_counts.get(ip, packet_count)
    prev_t = last_times.get(ip, now)

    growth = (packet_count - prev_c) / max(now - prev_t, 1)

    last_counts[ip] = packet_count
    last_times[ip] = now

    avg = sum(baseline_packets[ip]) / len(baseline_packets[ip])

    data = pd.DataFrame({"packets_per_ip":[packet_count]})
    pred = model.predict(data)[0]

    # ---- AI + behaviour anomaly ----
    if (pred == -1 or packet_count > avg * 2) and ip not in blocked_ips:

        attack, mitre, conf = classify_attack(packet_count)

        if growth > 60: risk = 3
        elif growth > 25: risk = 2
        else: risk = 1

        if not DEMO_MODE and risk == 3:
            block_ip(ip)

        blocked_ips.add(ip)

        # ---- SOC Escalation ----
        add_risk(risk)
        meter_add_risk(risk * 8)
        update_attack(ip, attack, ["LOW","MEDIUM","HIGH"][risk-1])

        log_incident(
            ip, packet_count,
            ["LOW","MEDIUM","HIGH"][risk-1],
            f"{attack}|MITRE:{mitre}|CONF:{conf*100:.0f}%"
        )

def block_ip(ip):
    cmd = f'netsh advfirewall firewall add rule name="Block_{ip}" dir=in action=block remoteip={ip}'
    subprocess.run(cmd, shell=True)
