import tkinter as tk

toast = None

def show_toast(message):
    global toast
    if toast:
        return

    toast = tk.Toplevel()
    toast.overrideredirect(True)
    toast.attributes("-topmost", True)
    toast.configure(bg="#7f1d1d")

    screen_w = toast.winfo_screenwidth()
    screen_h = toast.winfo_screenheight()
    toast.geometry(f"350x110+{screen_w-370}+{screen_h-160}")

    tk.Label(toast, text="INSIDER THREAT ALERT",
             bg="#7f1d1d", fg="white",
             font=("Segoe UI",12,"bold")).pack(pady=5)

    tk.Label(toast, text=message,
             bg="#7f1d1d", fg="white",
             font=("Consolas",10)).pack()

    toast.after(5000, close_toast)

def close_toast():
    global toast
    if toast:
        toast.destroy()
        toast = None
