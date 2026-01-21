from scapy.all import sniff, IP
import psutil
import time

packet_count = 0

def process_packet(packet):
    global packet_count
    if packet.haslayer(IP):
        packet_count += 1
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"[{packet_count}] {src} -> {dst} | Protocol: {proto}")

print("Starting Network Packet Capture...")
sniff(filter="ip", prn=process_packet, store=False)
