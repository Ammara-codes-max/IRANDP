import tkinter as tk
from threat_intel import lookup_ip

def open_intel_window(ip=None):
    win = tk.Toplevel()
    win.title("IRANDP – Global Threat Intelligence")
    win.geometry("650x520")
    win.configure(bg="#0B1220")

    # ===== HEADER =====
    tk.Label(win,text="Global Threat Intelligence Lookup",
             bg="#0B1220",fg="#38BDF8",
             font=("Segoe UI",16,"bold")).pack(pady=6)

    tk.Label(win,text="What you are seeing: This checks whether an IP is globally reported as malicious.",
             bg="#0B1220",fg="#E5E7EB",
             font=("Segoe UI",10)).pack()

    # ===== INPUT =====
    frame=tk.Frame(win,bg="#0B1220")
    frame.pack(pady=8)

    entry=tk.Entry(frame,width=28,font=("Segoe UI",11))
    entry.pack(side="left",padx=6)

    if ip:
        entry.insert(0,ip)

    # ===== INSIGHT =====
    insight=tk.Label(win,text="INSIGHT: Enter an IP and click Analyze.",
                     bg="#020617",fg="#FACC15",
                     font=("Segoe UI",11,"bold"))
    insight.pack(fill="x",padx=10,pady=6)

    # ===== RESULT BOX =====
    box=tk.Text(win,bg="#020617",fg="#E5E7EB",font=("Consolas",10))
    box.pack(fill="both",expand=True,padx=10,pady=8)

    def analyze():
        ip=entry.get().strip()
        box.delete(1.0,tk.END)

        data=lookup_ip(ip)
        if not data:
            insight.config(text="INSIGHT: Unable to retrieve threat intelligence.")
            return

        score=data.get("abuseConfidenceScore",0)
        country=data.get("countryCode","NA")
        isp=data.get("isp","Unknown")

        box.insert(tk.END,f"IP Address: {ip}\n")
        box.insert(tk.END,f"Country: {country}\n")
        box.insert(tk.END,f"ISP: {isp}\n")
        box.insert(tk.END,f"Abuse Confidence Score: {score}%\n\n")

        if score>50:
            insight.config(text="INSIGHT: This IP is reported as HIGH-RISK globally.")
        elif score>10:
            insight.config(text="INSIGHT: This IP has suspicious reputation.")
        else:
            insight.config(text="INSIGHT: This IP has clean or low-risk reputation.")

    tk.Button(frame,text="Analyze",
              bg="#2563EB",fg="white",
              font=("Segoe UI",10,"bold"),
              command=analyze).pack(side="left",padx=6)
