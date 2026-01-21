def identify_attacker(packet_rate, insider=False):
    if insider:
        return "INSIDER THREAT ACTOR"
    if packet_rate > 40:
        return "BOTNET NODE"
    if packet_rate > 15:
        return "RECONNAISSANCE SCANNER"
    return "LOW-RISK ACTOR"
