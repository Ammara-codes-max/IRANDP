import tkinter as tk
from timeline_engine import get_timeline

def open_timeline_window():
    win = tk.Toplevel()
    win.title("IRANDP – SOC Attack Timeline")
    win.geometry("760x520")
    win.configure(bg="#0B1220")

    seen = set()   # each window keeps its own memory

    tk.Label(win, text="SOC Attack Timeline Reconstruction",
             bg="#0B1220", fg="#38BDF8",
             font=("Segoe UI",16,"bold")).pack(pady=6)

    tk.Label(win, text="This window rebuilds how the cyber attack evolved in real time.",
             bg="#0B1220", fg="#E5E7EB",
             font=("Segoe UI",10)).pack()

    insight_frame = tk.Frame(win, bg="#020617", bd=2, relief="solid")
    insight_frame.pack(fill="x", padx=10, pady=8)

    insight_label = tk.Label(insight_frame,
                             text="INSIGHT: Learning network behaviour...",
                             bg="#020617", fg="#FACC15",
                             font=("Segoe UI",11,"bold"))
    insight_label.pack(anchor="w", padx=6, pady=4)

    tk.Label(win, text="Forensic Timeline:",
             bg="#0B1220", fg="#22C55E",
             font=("Segoe UI",12,"bold")).pack(anchor="w", padx=12)

    box = tk.Text(win, bg="#020617", fg="#E5E7EB",
                  font=("Consolas",10))
    box.pack(fill="both", expand=True, padx=10, pady=6)

    def refresh():
        data = get_timeline()

        for line in data:
            if line not in seen:
                seen.add(line)

                l = line.lower()

                if "containment" in l or "blocked" in l:
                    box.insert(tk.END, "🟥 " + line + "\n")
                    insight_label.config(text="INSIGHT: IRANDP executed autonomous containment.")
                elif "attack" in l or "flood" in l or "scan" in l:
                    box.insert(tk.END, "🟧 " + line + "\n")
                    insight_label.config(text="INSIGHT: Active intrusion phase detected.")
                elif "spike" in l:
                    box.insert(tk.END, "🟨 " + line + "\n")
                    insight_label.config(text="INSIGHT: Abnormal traffic spike under analysis.")
                elif "learning" in l:
                    box.insert(tk.END, "🟦 " + line + "\n")
                    insight_label.config(text="INSIGHT: Baseline behaviour learning phase.")
                else:
                    box.insert(tk.END, "🟩 " + line + "\n")
                    insight_label.config(text="INSIGHT: Monitoring live network activity.")

                box.see(tk.END)

        win.after(1500, refresh)

    refresh()
