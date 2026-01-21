import tkinter as tk
from session_tracker import get_sessions

def open_session_window():
    win = tk.Toplevel()
    win.title("IRANDP – Attack Session Timeline")
    win.geometry("600x420")
    win.configure(bg="#0B1220")

    tk.Label(win, text="Attack Session Timeline",
             bg="#0B1220", fg="#F59E0B",
             font=("Segoe UI", 14, "bold")).pack(pady=10)

    box = tk.Text(win, bg="#020617", fg="#F59E0B",
                  font=("Consolas", 10))
    box.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh():
        box.delete(1.0, tk.END)
        sessions = get_sessions()
        for ip, data in sessions.items():
            duration = int(data["last"] - data["start"])
            box.insert(tk.END,
                f"{ip} | Duration: {duration}s | Packets: {data['count']}\n")
        win.after(2000, refresh)

    refresh()
