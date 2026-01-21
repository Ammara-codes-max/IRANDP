import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from threat_meter import get_score
import time

scores = []
timestamps = []

def open_risk_window():
    win = tk.Toplevel()
    win.title("IRANDP – Organizational Risk Trend")
    win.geometry("700x500")
    win.configure(bg="#0B1220")

    tk.Label(win,text="Organizational Risk Trend",
             bg="#0B1220",fg="#38BDF8",
             font=("Segoe UI",16,"bold")).pack(pady=6)

    tk.Label(win,text="Live organizational cyber-risk evolution over time.",
             bg="#0B1220",fg="#E5E7EB",
             font=("Segoe UI",10)).pack()

    insight=tk.Label(win,text="INSIGHT: Establishing baseline.",
                     bg="#020617",fg="#FACC15",
                     font=("Segoe UI",11,"bold"))
    insight.pack(fill="x",padx=10,pady=6)

    fig,ax = plt.subplots()
    fig.set_facecolor("#0B1220")
    ax.set_facecolor("#020617")

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    def refresh():
        now = time.time()
        score = get_score()

        if score > 0:
            scores.append(score)
            timestamps.append(now)

        # Keep last 60 seconds only
        while timestamps and now - timestamps[0] > 60:
            timestamps.pop(0)
            scores.pop(0)

        ax.clear()
        ax.plot(scores)
        ax.set_title("Live Organizational Risk Trend", color="white")
        ax.set_ylabel("Risk Score", color="white")
        ax.set_xlabel("Time", color="white")
        ax.tick_params(colors="white")

        # ---- Intelligent Insight ----
        if len(scores) >= 5:
            slope = scores[-1] - scores[-5]
            if slope > 15:
                insight.config(text="INSIGHT: Risk escalating rapidly – possible attack in progress.")
            elif slope > 5:
                insight.config(text="INSIGHT: Risk slowly increasing – monitor closely.")
            elif scores[-1] < 25:
                insight.config(text="INSIGHT: Risk stable – environment under control.")
            else:
                insight.config(text="INSIGHT: Risk fluctuating within normal range.")

        canvas.draw()
        win.after(1000, refresh)

    refresh()
