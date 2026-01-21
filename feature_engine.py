from scapy.all import sniff, IP
from collections import defaultdict
from containment_engine import analyze_and_contain

ip_stats = defaultdict(int)

def process_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        ip_stats[src] += 1

        if ip_stats[src] % 20 == 0:
            analyze_and_contain(src, ip_stats[src])

print("Feature Engine with Containment Started...")
sniff(filter="ip", prn=process_packet, store=False)
