import tkinter as tk
from attack_stats import get_attack_stats

def open_heatmap():
    win = tk.Toplevel()
    win.title("IRANDP – Threat Heatmap Analytics")
    win.geometry("700x480")
    win.configure(bg="#0B1220")

    tk.Label(win,text="Threat Heatmap Analytics",
             bg="#0B1220",fg="#EF4444",
             font=("Segoe UI",14,"bold")).pack(pady=10)

    box = tk.Text(win,bg="#020617",fg="#EF4444",font=("Consolas",10))
    box.pack(fill="both",expand=True,padx=10,pady=10)

    def refresh():
        box.delete(1.0,tk.END)
        stats = get_attack_stats()
        for ip,data in stats.items():
            box.insert(tk.END,
                f"{ip} | {data['attack']} | {data['severity']} | Hits:{data['count']}\n")
        win.after(2000,refresh)

    refresh()
