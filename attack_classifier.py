def classify_attack(packet_count):
    if packet_count > 80:
        return "SYN Flood", "T1499", 0.95
    elif packet_count > 50:
        return "Port Scanning", "T1046", 0.92
    elif packet_count > 30:
        return "ICMP Flood", "T1499", 0.88
    else:
        return "Unknown Anomaly", "N/A", 0.70
