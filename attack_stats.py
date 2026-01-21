attack_db = {}

def update_attack(ip, attack, severity):
    if ip not in attack_db:
        attack_db[ip] = {"attack": attack, "severity": severity, "count": 1}
    else:
        attack_db[ip]["count"] += 1

def get_attack_stats():
    return attack_db
