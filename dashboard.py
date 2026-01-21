app_running = True
import tkinter as tk
import threading, time, winsound
from scapy.all import sniff, IP

from containment_engine import analyze_and_contain, blocked_ips
from attack_classifier import classify_attack
from forensic_report import generate_report
from risk_graph_window import open_risk_window
from threat_meter import get_score, add_risk
from attack_heatmap_window import open_heatmap
from intel_window import open_intel_window
from timeline_engine import log_event
from timeline_window import open_timeline_window
from geo_map_window import add_point, open_geo_window
from toast_alert import show_toast
from compliance_engine import get_risk
from email_alert import send_alert

START_TIME = time.time()
WARMUP = 10
current_state = "LEARNING"

root = tk.Tk()
root.title("IRANDP – Intelligent Rule-Based Autonomous Network Defense Platform")
root.geometry("1500x920")
root.configure(bg="#0B1220")

running = False
ip_stats = {}
pps = 0
last_time = time.time()
threat_counter = 0

# ===== MISSION CONTROL BAR =====
mission = tk.Frame(root, bg="#020617", height=55)
mission.pack(fill="x")

threat_gauge = tk.Label(mission, text="THREAT LEVEL: 0%",
                        bg="#020617", fg="#22C55E",
                        font=("Segoe UI",12,"bold"))
threat_gauge.pack(side="left", padx=20)

threat_label = tk.Label(mission, text="ACTIVE THREATS: 0",
                        bg="#020617", fg="#EF4444",
                        font=("Segoe UI",12,"bold"))
threat_label.pack(side="left", padx=20)

defense_label = tk.Label(mission, text="DEFENSE MODE: LOW",
                         bg="#020617", fg="#38BDF8",
                         font=("Segoe UI",12,"bold"))
defense_label.pack(side="right", padx=20)

# ===== LAYOUT =====
container = tk.Frame(root, bg="#0B1220")
container.pack(fill="both", expand=True)

sidebar = tk.Frame(container, bg="#020617", width=220)
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="CONTROL PANEL",
         bg="#020617", fg="#38BDF8",
         font=("Segoe UI",12,"bold")).pack(pady=15)

def sbtn(t, cmd):
    return tk.Button(sidebar, text=t, bg="#1E293B", fg="white",
                     width=22, pady=6, command=cmd)

sbtn("Deploy Sensors", lambda: deploy()).pack(pady=5)
sbtn("Halt Sensors", lambda: halt()).pack(pady=5)
sbtn("SOC Timeline", open_timeline_window).pack(pady=5)
sbtn("Attack Geo Map", open_geo_window).pack(pady=5)
sbtn("View Risk Trend", open_risk_window).pack(pady=5)
sbtn("Threat Heatmap", open_heatmap).pack(pady=5)
sbtn("Global Threat Check", open_intel_window).pack(pady=5)
sbtn("Export Forensic PDF", generate_report).pack(pady=5)

content = tk.Frame(container, bg="#0B1220")
content.pack(side="left", fill="both", expand=True, padx=10)

tk.Label(content, text="IRANDP – Cyber Defense Command Center",
         bg="#0B1220", fg="#38BDF8",
         font=("Segoe UI",18,"bold")).pack(pady=6)

status = tk.StringVar(value="Sensors Offline")
tk.Label(content, textvariable=status, bg="#0B1220",
         fg="#22C55E", font=("Segoe UI",12)).pack()

main = tk.Frame(content, bg="#0B1220")
main.pack(pady=8)

def panel(t,c,r,cl,w,h):
    f=tk.Frame(main,bg="#020617",bd=2,relief="solid")
    tk.Label(f,text=t,bg="#020617",fg=c,
             font=("Segoe UI",12,"bold")).pack(anchor="w",padx=6)
    box=tk.Text(f,bg="#020617",fg=c,width=w,height=h,font=("Consolas",10))
    box.pack(padx=6,pady=5)
    f.grid(row=r,column=cl,padx=10,pady=10)
    return box

telemetry = panel("Network Telemetry","#38BDF8",0,0,45,15)
threats   = panel("Threat Intelligence","#EF4444",0,1,60,15)
actions   = panel("Autonomous Response","#F59E0B",1,0,45,12)
evidence  = panel("Forensic Intelligence","#22C55E",1,1,60,12)

stats=tk.Label(content,text="Packets/sec: 0",
               bg="#0B1220",fg="#38BDF8",font=("Consolas",12))
stats.pack()

# ===== BANNER UPDATE =====
def update_banner():
    global current_state
    score=get_score()
    threat_gauge.config(text=f"THREAT LEVEL: {score}%")

    if score>75:
        defense_label.config(text="DEFENSE MODE: HIGH",fg="#EF4444")
        if current_state!="ALERT": winsound.Beep(1800,400)
        current_state="ALERT"
    elif score>35:
        defense_label.config(text="DEFENSE MODE: MEDIUM",fg="#F59E0B")
        current_state="WARNING"
    else:
        defense_label.config(text="DEFENSE MODE: LOW",fg="#22C55E")
        current_state="NORMAL"

    root.after(1000,update_banner)

update_banner()

# ===== PACKET HANDLER =====
def packet_handler(pkt):
    global pps,threat_counter
    if not running or not pkt.haslayer(IP): return

    src=pkt[IP].src
    ip_stats[src]=ip_stats.get(src,0)+1
    pps+=1

    telemetry.delete(1.0,tk.END)
    for ip,c in sorted(ip_stats.items(),key=lambda x:x[1],reverse=True)[:6]:
        telemetry.insert(tk.END,f"{ip} → {c}\n")

    if ip_stats[src]%8==0:
        log_event(f"Traffic spike from {src}")
        analyze_and_contain(src,ip_stats[src])
        add_risk(8)
        add_point(src)

        atk,mit,_=classify_attack(ip_stats[src])
        threats.insert(tk.END,f"[THREAT] {src} | {atk} | MITRE:{mit}\n")

        threat_counter+=1
        threat_label.config(text=f"ACTIVE THREATS: {threat_counter}")

        if src in blocked_ips:
            actions.insert(tk.END,f"[ACTION] Containment executed for {src}\n")
            evidence.insert(tk.END,f"[FORENSIC] IP:{src} RATE:{ip_stats[src]}\n")
            log_event(f"Containment executed on {src}")
            show_toast(f"ATTACK BLOCKED\nIP:{src}")
            send_alert(
            "🚨 IRANDP ALERT – Network Attack Blocked",
            f"IP Address: {src}\nPackets: {ip_stats[src]}\nAction: Automatically Blocked")
            


def sniff_thread():
    sniff(filter="ip",
          iface="\\Device\\NPF_{ACABEBD3-945C-4A78-AAE3-79B483872145}",
          prn=packet_handler,store=False)

def deploy():
    global running
    running=True
    status.set("Sensors Active")
    threading.Thread(target=sniff_thread,daemon=True).start()

def halt():
    global running
    running=False
    status.set("Sensors Offline")

root.mainloop()
